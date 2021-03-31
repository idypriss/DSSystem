using System;
using System.Drawing;
using System.Linq;

namespace SsdWebApi
{
    public class Forecast
    {
        public Forecast()
        {

        }

        public string forecastSARIMAindex(string attribute)
        {
            string res = "\"text\":\"";
            string interpreter = "C:/Users/Hp/anaconda3/envs/opanalytics/python.exe";
            string environment = "opanalytics";
            int timeout = 10000;
            PythonRunner pr = new PythonRunner(interpreter, environment, timeout);
            Bitmap bmp = null;
            
            try
            {
                string command = $"Models/ForcastSerie.py";
                string[] indices = new string[]{"SP_500", "FTSE_MIB", "GOLD_SPOT", "MSCI_EM", "MSCI_EURO", "All_Bonds", "US_Treasury"};
                
                if (indices.Contains(attribute)) {
                    command = command + " " + attribute;
                }
                string list = pr.runDosCommands(command);

                if (string.IsNullOrWhiteSpace(list))
                {
                    Console.WriteLine("Error in the script call");
                    return res;
                }

                string[] lines = list.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
                string strBitmaps = "[";
                foreach (string s in lines)
                {
                    if (s.StartsWith("MAPE") || s.StartsWith("Actual") || s.StartsWith("Return") || s.StartsWith("Devst") || s.StartsWith("Portfolio"))
                    {
                        Console.WriteLine(s);
                        res += (s+"\\n");
                    }

                    if (s.StartsWith("b'"))
                    {
                        strBitmaps += "\""+ s.Trim().Substring(s.IndexOf("b'"))+"\",";
                        try
                        {
                            bmp = pr.FromPythonBase64String(s.Trim().Substring(s.IndexOf("b'")));
                        }
                        catch (Exception e)
                        {
                            throw new Exception("Error while creating image from Python script", e);
                        }
                    }
                }
				strBitmaps = strBitmaps.TrimEnd(',');
				strBitmaps += "]";

                //strBitmap = strBitmap.Substring(strBitmap.IndexOf("b'")); // begin of binary image
                // strBitmap = strBitmap.Remove(strBitmap.Length-4).Trim(); // remove "exit" at the end
                res += "\",\"img\":"+strBitmaps;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

            return res;
        } 
    }
}