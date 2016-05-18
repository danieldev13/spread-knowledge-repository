using System;

using task_runner.processors;
using task_runner.enums;

namespace task_runner {
    public class FactoryManager {
        private FactoryProcess factory = new FactoryProcess(5000);
        
        public FactoryManager() {
            factory.OnTimeoutReached += new TimeoutReachedHandler(Factory_OnTimeoutReached);
            factory.OnStatusChanged += new StatusChangedHandler(Factory_OnStatusChanged);
            factory.OnProcessFinished += new ProcessFinishedHandler(Factory_OnProcessFinished);
        }
        
        void Factory_OnProcessFinished()
        {
            Console.WriteLine("Process finished.");
        }
        void Factory_OnStatusChanged(FactoryProcessStatus status)
        {
            Console.WriteLine("Status changed to: {0}", status);
        }
        void Factory_OnTimeoutReached()
        {
            Console.WriteLine("Timeout reached...");
        }
        public void buttonStart_Click()
        {
            factory.Start();
        }
    
        public void buttonPause_Click()
        {
            factory.Pause();
        }
        public void buttonResume_Click()
        {
            factory.Resume();
        }
    
        public void buttonStop_Click()
        {
            factory.Stop();
        }
        public void buttonRestart_Click()
        {
            factory.Restart();
        }
    }
}