using System;

namespace SerilogWrapperApi.Models {
    public class LogInfo {
        public string message { get; set; }
        public object exceptionData { get; set; }
        public int logType { get; set; }
    }
}