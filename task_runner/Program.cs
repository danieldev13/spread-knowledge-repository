using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace task_runner
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("!!! Factory Processor Example - STARTING !!!");
            
            var manager = new FactoryManager();
            
            manager.buttonStart_Click();
            Console.WriteLine("Press enter to continue...");
            Console.ReadLine();
            
            manager.buttonPause_Click();
            Console.WriteLine("Press enter to continue...");
            Console.ReadLine();
            
            manager.buttonResume_Click();
            Console.WriteLine("Press enter to continue...");
            Console.ReadLine();
            
            manager.buttonRestart_Click();
            Console.WriteLine("Press enter to continue...");
            Console.ReadLine();
            
            manager.buttonStop_Click();
            Console.WriteLine("Press enter to continue...");
            Console.ReadLine();
            
            Console.WriteLine("!!! Factory Processor Example - FINISHED !!!");
            Console.Read();
        }
    }
}
