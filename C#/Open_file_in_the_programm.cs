using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Open_file_in_the_programm
{
    class Program
    {
        static void Print_with_accuracy(double a, int x, string l)
        {
            string s = a.ToString();
            //Console.WriteLine("a = {0:N8}", a);
            //Console.WriteLine("s = {0}", s);

            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == ',')
                {
                    string[] ss = s.Split(',');

                    if (x < ss[1].Length)
                    {
                        ss[1] = ss[1].Substring(0, x);
                        Console.WriteLine("{0} = {1},{2}", l, ss[0], ss[1]);
                    }
                    else
                    {
                        Console.WriteLine("{0} = {1}", l, a);
                    }
                    return;
                }
            }
            Console.WriteLine("{0} = {1}", l, a);
        }
        static void Main(string[] args)
        {
            double a = 4.24222342424;
            int x = 0;
            Console.WriteLine("Введите количество желаемых знаков после запятой:");
            x = int.Parse(Console.ReadLine());

            Print_with_accuracy(a, x, "a");
        }
    }
}
