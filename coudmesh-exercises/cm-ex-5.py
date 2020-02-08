from cloudmesh.common.StopWatch import StopWatch
from time import sleep

StopWatch.start("cm-ex-1")
sleep(1)
StopWatch.stop("cm-ex-1")

StopWatch.benchmark()
