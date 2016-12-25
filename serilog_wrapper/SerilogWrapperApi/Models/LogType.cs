using System;

namespace SerilogWrapperApi.Models {
    public enum LogType : int
    {
        Information = 0,
        Error = 1,
        Warning = 2,
        Debug = 3,
        Fatal = 4
    }
}