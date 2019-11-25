import threading
import webcam_conn
import face_detect
import simple_camera
from queue import Queue

def creator(data, q):
    print("Createing data and putting it on the queue")
    print("\n")
    #face_detect.faceDetect()
    simple_camera.show_camera()
    for item in data:
        evt = threading.Event()
        q.put((item, evt))
        print('creator')
        evt.wait()

def consumer(q):
    webcam_conn.human_detect()
    while True:
        data, evt = q.get()
        print('~')
        processed = data * 5
        print('~~')
        print('\n')
        evt.set()
        q.task_done()

if __name__ == '__main__':
    q = Queue()

    data=[7, 14, 39, 59, 77, 1, 109, 99, 167, 920, 1035]

    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=consumer, args=(q,))
    thread_one.start()
    thread_two.start()
    q.join()