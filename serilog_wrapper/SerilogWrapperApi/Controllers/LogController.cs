using System;
using Microsoft.AspNetCore.Mvc;
using Serilog;
using SerilogWrapperApi.Models;

namespace SerilogWrapperApi.Controllers
{
    [Route("api/[controller]")]
    public class LogController : Controller
    {
        // POST api/values
        [HttpPost]
        public void Post([FromBody]LogInfo message)
        {
            try
            {
                var exception = new Exception(message.exceptionData.ToString());

                if (message.logType == (int)LogType.Information) {
                    Log.Logger.Information(message.message);
                } 
                else if (message.logType == (int)LogType.Error) {
                    Log.Logger.Error(exception, message.message);
                }
                else if (message.logType == (int)LogType.Fatal) {
                    Log.Logger.Fatal(exception, message.message);
                }
                else if (message.logType == (int)LogType.Warning) {
                    Log.Logger.Warning(exception, message.message);
                }
                else if (message.logType == (int)LogType.Debug) {
                    Log.Logger.Debug(exception, message.message);
                }
            }
            catch (Exception)
            {
                throw;
            }
        }
    }
}
