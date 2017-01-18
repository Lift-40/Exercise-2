package main

import (
    . "fmt"
    "runtime"
	"sync"
    "time"
)

var hopefullyZero int32
var mut sync.Mutex

func thread1() {
	for i := 0; i < 1000001; i++ {
		mut.Lock()
		hopefullyZero++
		mut.Unlock()
	}
}

func thread2() {
	for i := 0; i < 1000000; i++ {
		mut.Lock()
		hopefullyZero--
		mut.Unlock()
	}
}

func main() {
    runtime.GOMAXPROCS(runtime.NumCPU())
						
    go thread1()
	go thread2()
	
    time.Sleep(1*time.Second)
	Println("Result: ")
    Println(hopefullyZero)
}