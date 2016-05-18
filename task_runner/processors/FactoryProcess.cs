using System;
using System.Threading;

using task_runner.enums;

namespace task_runner.processors {
    public delegate void TimeoutReachedHandler();
    public delegate void StatusChangedHandler(FactoryProcessStatus status);
    public delegate void ProcessFinishedHandler();
    public delegate void ProcessPausedHandler();
    public delegate void ProcessStartedHandler();
    public delegate void RunProcessDelegate();
    public class FactoryProcess
    {
        private bool _mustRestart;
        private bool _stopProcess;
        public int Timeout { get; set; }
    
        private FactoryProcessStatus _status;
        public FactoryProcessStatus Status
        {
            get
            {
                return this._status;
            }
            set
            {
                this._status = value;
                if (OnStatusChanged != null)
                    OnStatusChanged(this.Status);
            }
        }
        public event TimeoutReachedHandler OnTimeoutReached;
        public event StatusChangedHandler OnStatusChanged;
        public event ProcessFinishedHandler OnProcessFinished;
        public event ProcessPausedHandler OnProcessPaused;
        public event ProcessStartedHandler OnProcessStarted;
    
        public FactoryProcess(int timeout = 300000)
        {
            this._stopProcess = false;
            this.Timeout = timeout;
        }
        public void Pause()
        {
            this.Status = FactoryProcessStatus.Pausing;
        }
        public void Restart()
        {
            this._mustRestart = true;
            this.Stop();
        }
        public void Resume()
        {
            this.Status = FactoryProcessStatus.Resuming;
        }
        public void Start()
        {
            this.Status = FactoryProcessStatus.Starting;
            this.RunProcessAsync();
        }
        public void Stop()
        {
            this.Status = FactoryProcessStatus.Stopping;
        }
        private void RunProcess()
        {
            while (!_stopProcess)
            {
                if (this.Status == FactoryProcessStatus.Stopping)
                {
                    this._stopProcess = true;
                    this.Status = FactoryProcessStatus.Stopped;
                }
                else if (this.Status == FactoryProcessStatus.Starting)
                {
                    this.Status = FactoryProcessStatus.Running;
                    this._stopProcess = false;
                }
                else if (this.Status == FactoryProcessStatus.Pausing)
                {
                    this.Status = FactoryProcessStatus.Paused;
                    this._stopProcess = false;
                    if (OnProcessPaused != null)
                        OnProcessPaused();
                }
                else if (this.Status == FactoryProcessStatus.Resuming)
                {
                    this.Status = FactoryProcessStatus.Running;
                    this._stopProcess = false;
                }
    
                if (this.Status == FactoryProcessStatus.Running)
                {
                    if (this.OnTimeoutReached != null)
                        this.OnTimeoutReached();
                }
    
                if (this.Status == FactoryProcessStatus.Running || this.Status == FactoryProcessStatus.Paused)
                {
                    Thread.Sleep(this.Timeout);
                }
            }
        }
        private void RunProcessAsync()
        {
            RunProcessDelegate process = new RunProcessDelegate(RunProcess);
            AsyncCallback callback = delegate
            {
                this._stopProcess = false;
                if (OnProcessFinished != null)
                    OnProcessFinished();
    
                if (this._mustRestart)
                {
                    this._mustRestart = false;
                    this.Start();
                }
            };
    
            process.BeginInvoke(callback, null);
    
            if (OnProcessStarted != null)
                OnProcessStarted();
        }
    }
}