namespace ProgressBar
{
    partial class Form1
    {
        /// <summary>
        /// Variabile di progettazione necessaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Pulire le risorse in uso.
        /// </summary>
        /// <param name="disposing">ha valore true se le risorse gestite devono essere eliminate, false in caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Codice generato da Progettazione Windows Form

        /// <summary>
        /// Metodo necessario per il supporto della finestra di progettazione. Non modificare
        /// il contenuto del metodo con l'editor di codice.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.ProgBar = new System.Windows.Forms.ProgressBar();
            this.elapsed = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // ProgBar
            // 
            this.ProgBar.Location = new System.Drawing.Point(13, 13);
            this.ProgBar.Name = "ProgBar";
            this.ProgBar.Size = new System.Drawing.Size(559, 36);
            this.ProgBar.TabIndex = 0;
            this.ProgBar.Click += new System.EventHandler(this.ProgBar_Click);
            // 
            // elapsed
            // 
            this.elapsed.AutoSize = true;
            this.elapsed.Location = new System.Drawing.Point(10, 69);
            this.elapsed.Name = "elapsed";
            this.elapsed.Size = new System.Drawing.Size(0, 13);
            this.elapsed.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(584, 91);
            this.Controls.Add(this.elapsed);
            this.Controls.Add(this.ProgBar);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Progress";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ProgressBar ProgBar;
        private System.Windows.Forms.Label elapsed;
    }
}

