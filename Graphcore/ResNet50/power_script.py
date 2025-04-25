import multiprocessing
import os
import gcipuinfo
import time

class ipuPowerProbe():
    def __init__(self,interval, extra_ipu=False):
        '''
        set extra_ipu to True if the machine has more
        ipus than you have used in your program. Other
        than that, use extra_ipu=False
        '''
        self.interval = multiprocessing.Value('d', interval)
        self.len = int(1000/interval)
        self.powers = multiprocessing.Array('d', self.len)
        self.times = multiprocessing.Array('d', self.len)
        self.process = None
        self.prevTime = multiprocessing.Value('d',time.time())
        self.halt = multiprocessing.Value('i',1)
        self.count = multiprocessing.Value('i',0)
        self.isrunning = multiprocessing.Value('i',0)
        self.alive = multiprocessing.Value('i',0)
        self.pid = multiprocessing.Value('i', os.getpid())
        self.extra_ipu = extra_ipu
        self.init()

    def _getPower_without_extra_ipu(self, powers, times, count, halt, alive, isrunning, prevTime, interval):
        ipu_info = gcipuinfo.gcipuinfo()
        while (alive.value):
            while (not halt.value):
                isrunning.value = 1
                device_powers = ipu_info.getNamedAttributeForAll(gcipuinfo.IpuPower)
                power = sum([float(p[:-1]) for p in device_powers if p != 'N/A'])
                new_time = time.time()
                while (new_time-prevTime.value < interval.value):
                    new_time = time.time()
                powers[count.value] = power
                times[count.value] = new_time-prevTime.value
                count.value += 1
                prevTime.value = new_time
                isrunning.value = 0

    def _getPower_with_extra_ipu(self, powers, times, count, pid, halt, alive, isrunning, prevTime, interval):
        ipu_info = gcipuinfo.gcipuinfo()
        while (alive.value):
            while (not halt.value):
                isrunning.value = 1
                dev_dicts = [dict(d) for d in ipu_info.getDevices()]
                zipped_pid_pwr = [(int(dev.get(gcipuinfo.UserProcessId, 0)), dev.get(gcipuinfo.IpuPower)) for dev in dev_dicts]
                power = sum([float(dpwr[:-1]) for dpid, dpwr in zipped_pid_pwr if dpid == pid.value and dpwr != "N/A"])
                new_time = time.time()
                while (new_time-prevTime.value < interval.value):
                    new_time = time.time()
                powers[count.value] = power
                times[count.value] = new_time-prevTime.value
                count.value += 1
                prevTime.value = new_time
                isrunning.value = 0

    def init(self):
        self.halt.value = 1
        self.alive.value = 1
        if self.extra_ipu:
            self.process = multiprocessing.Process(target = self._getPower_with_extra_ipu, args = (self.powers, self.times,
                self.count, self.pid, self.halt, self.alive, self.isrunning, self.prevTime, self.interval))
        else:
            self.process = multiprocessing.Process(target = self._getPower_without_extra_ipu, args = (self.powers, self.times,
                self.count, self.halt, self.alive, self.isrunning, self.prevTime, self.interval))
        self.process.start()

    def start(self):
        self.count.value = 0
        self.prevTime.value = time.time()
        self.halt.value = 0

    def stop(self):
        self.halt.value = 1
        while (self.isrunning.value):
            pass
        return self.powers[:self.count.value], self.times[:self.count.value]

    def destroy(self):
        self.alive.value = 0
        self.process.join()
