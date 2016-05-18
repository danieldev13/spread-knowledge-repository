using System;

namespace task_runner.enums 
{
    public enum FactoryProcessStatus
    {
        Stopped = 0,
        Stopping = 1,
        Starting = 2,
        Running = 3,
        Pausing = 4,
        Paused = 5,
        Resuming = 6,
    }    
}

