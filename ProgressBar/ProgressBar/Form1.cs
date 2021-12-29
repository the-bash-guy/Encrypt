using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using System.Diagnostics;

namespace ProgressBar
{
    public partial class Form1 : Form
    {
        public static string[] files;
        public static int size1;
        public static int size2;
        public static int percent;
        public Form1()
        {
            InitializeComponent();
        }

        private void ProgBar_Click(object sender, EventArgs e)
        {
            string credits = "Creator: https://github.com/DogLife2007 \nOfficial Site: https://noescape1151.ddns.net";
            MessageBox.Show(credits);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            files = Environment.GetCommandLineArgs();
            long insize = (new FileInfo(files[1]).Length / 1024) / 1024;
            size1 = (int)insize;
            this.ProgBar.Maximum = size1;
            Thread timer = new Thread(() => Elapsed_time());
            Thread progress = new Thread(() => Progress());
            timer.Start();
            progress.Start();
        }

        private void Progress()
        {
            while (this.ProgBar.Value < (size1 - 0.2))
            {
                long outsize = (new FileInfo(files[2]).Length / 1024) / 1024;
                size2 = (int)outsize;
                this.ProgBar.Value = size2;
            }
            Application.Exit();
        }

        private void Elapsed_time()
        {
            Stopwatch time_elapsed = new Stopwatch();
            time_elapsed.Start();
            while (this.ProgBar.Value < (size1 - 0.2))
            {
                TimeSpan elapsedtime = time_elapsed.Elapsed;
                this.elapsed.Text = "Elapsed time: " + elapsedtime.ToString(@"dd\.hh\:mm\:ss");
            }
            time_elapsed.Stop();
            Application.Exit();
        }
    }
}
