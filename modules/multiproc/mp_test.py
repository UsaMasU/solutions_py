import multiprocessing as mp
import time
from random import randint
from pprint import pprint


def monitor(_proc_q: mp.Queue, _proc_m_d: mp.Manager, _proc_p: mp.Pipe):
    loop = True
    data_lst = list()

    tmp_proc_num = randint(0, 10)
    tmp_m_d = _proc_m_d[tmp_proc_num]
    tmp_m_d['flag'] = True
    _proc_m_d[tmp_proc_num] = tmp_m_d

    while loop:
        if not _proc_q.empty():
            get_data = _proc_q.get()
            if 'cmd' in get_data:
                if get_data['cmd'] == 'start':
                    print("start monitor")
                elif get_data['cmd'] == 'stop':
                    print("stop monitor")
                    loop = False
            data_lst.append(get_data)
    _proc_p.send(data_lst)


def job(_proc_l: mp.Lock, _proc_q: mp.Queue, _proc_m_d: mp.Manager, _proc_num):
    with _proc_l:
        _data = dict()

        time_job = randint(0, 10)
        print(f"job {_proc_num} start:")
        print(f"    job {_proc_num} is awaiting for {time_job} sec...")
        time.sleep(time_job)

        _data['num'] = _proc_num
        _data['time'] = time_job
        if _proc_m_d[_proc_num]['flag']:
            _data['flag'] = False
            _data['response'] = f"Hello from proc {_proc_num}"
        else:
            _data['flag'] = _proc_m_d[_proc_num]['flag']

        _proc_q.put(_data)
        _proc_m_d[_proc_num] = _data
    print(f"job {_proc_num} stop:")


if __name__ == '__main__':
    pool_max = 4
    proc_max = 10
    proc_lst = range(proc_max)
    pool = mp.Pool(pool_max)
    proc_m = mp.Manager()
    proc_m_d = proc_m.dict()
    proc_l = proc_m.Lock()
    proc_q = proc_m.Queue()
    proc_p_rcv, proc_p_snd = mp.Pipe()

    proc_data = dict()
    for i in range(proc_max):
        proc_data['num'] = i
        proc_data['time'] = 0
        proc_data['flag'] = False
        proc_m_d[i] = proc_data

    for i in proc_m_d.items():
        print(i)

    mon = mp.Process(target=monitor, args=(proc_q, proc_m_d, proc_p_snd))
    mon.start()

    print("start pool of jobs")
    proc_q.put({'cmd': 'start'})

    for proc_n in proc_lst:
        print("start job:", proc_n)
        pool.apply_async(job, [proc_l, proc_q, proc_m_d, proc_n])
        time.sleep(3)

    pool.close()
    pool.join()

    proc_q.put({'cmd': 'stop'})
    mon.join()

    print("result from pipe:")
    data = proc_p_rcv.recv()
    pprint(data)

    print("result from manager:")
    for i in proc_m_d.items():
        print(i)
