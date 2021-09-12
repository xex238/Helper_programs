using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Read_matrix_from_file_v_1._0
{
    class Class
    {
        // Чтение матрицы с файла
        static int[,] Input(out int n, string open_string)
        {
            StreamReader file = new StreamReader(open_string);
            string s = file.ReadToEnd();
            file.Close();
            string[] line = s.Split('\n');
            string[] column = line[0].Split(' ');
            int[,] a = new int[line.Length, column.Length];
            int t = 0;
            n = 0;
            for (int i = 0; i < line.Length; i++)
            {
                column = line[i].Split(' ');
                for (int j = 0; j < column.Length; j++)
                {
                    t = Convert.ToInt32(column[j]);
                    a[i, j] = t;
                }
            }
            return a;
        }
        // Вывод на экран матрицы а
        static void Print(int[,] a)
        {
            for (int i = 0; i < a.GetLength(0); i++)
            {
                for (int j = 0; j < a.GetLength(1); j++)
                {
                    Console.Write("{0} ", a[i, j]);
                }
                Console.WriteLine();
            }
        }
        // Подстчёт среднего арифметического значения
        static double Result(int[,] a)
        {
            int k = 0;
            double s = 0;
            for (int i = 0; i < a.GetLength(0); ++i)
            {
                for (int j = i + 1; j < a.GetLength(1); ++j)
                {
                    if (a[i, j] % 2 != 0)
                    {
                        ++k;
                        s += a[i, j];
                    }
                }
            }
            if (k != 0)
            {
                return s / k;
            }
            else
            {
                return 0;
            }
        }
        class Program
        {
            static void Open_file()
            {
                try
                {
                    int n;
                    int[,] myArray = Input(out n, "matrix.txt");
                    Console.WriteLine("Исходный массив:");
                    Print(myArray);

                    double rez = Result(myArray);
                    Console.WriteLine("Среднее арифметическое = {0:f2}", rez);
                }
                catch (FileNotFoundException)
                {
                    Console.WriteLine("Файл не найден");
                }
                catch (FormatException)
                {
                    Console.WriteLine("Неверное значение данных");
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine("Выход за границы массива");
                }
            }
            static void Main(string[] args)
            {
                Open_file();
            }
        }
    }
}
