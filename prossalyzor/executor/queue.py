from queue import Queue

from prossalyzor.core.common import PoolExecutor


class QueuedPoolExecutor(PoolExecutor):
    '''
    Pooled executor implementation based on queue
    mechanism.
    '''
    def __init__(self, context, q_size=1):
        super(QueuedPoolExecutor, self).__init__(context)
        self._task_q = Queue(q_size)
    
    def execute(self, task, callback):
        pass