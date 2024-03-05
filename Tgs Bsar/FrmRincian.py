import tkinter as tk
from tkinter import ttk, messagebox
from Rincian import Rincian

class FormRincian:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = ttk.Frame(self.parent, borderwidth=10)  # Use 'borderwidth' instead of 'bd'
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        # Label
        ttk.Label(mainFrame, text='No Parkir:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNoParkir = ttk.Entry(mainFrame) 
        self.txtNoParkir.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNoParkir.bind("<Return>", self.onCari)

        ttk.Label(mainFrame, text='Jenis Kendaraan:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtjeniskendaraan = ttk.Entry(mainFrame) 
        self.txtjeniskendaraan.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(mainFrame, teks='Jam Masuk:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtjammasuk = ttk.Entry(mainFrame) 
        self.txtjammasuk.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(mainFrame, teks='Jam Keluar:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtjamkeluar = ttk.Entry(mainFrame) 
        self.txtjamkeluar.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(mainFrame, text='Total Biaya:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txttotalbiaya = ttk.Entry(mainFrame) 
        self.txttotalbiaya.grid(row=2, column=1, padx=5, pady=5) 

        # Button
        self.btnSimpan = ttk.Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = ttk.Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = ttk.Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('noparkir', 'jeniskendaraan', 'jammasuk', 'jamkeluar', 'totalbiaya')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('noparkir', text='No Parkir')
        self.tree.column('noparkir', width="30")
        self.tree.heading('jeniskendaraan', text='Jenis Kendaraan')
        self.tree.column('jeniskendaraan', width="60")
        self.tree.heading('jammasuk', text='Jam Masuk')
        self.tree.column('jammasuk', width="30")
        self.tree.heading('jamkeluar', text='Jam Keluar')
        self.tree.column('jamkeluar', width="30")
        self.tree.column('totalbiaya', text='Total Biaya')
        self.tree.column('totalbiaya', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNoParkir.delete(0, tk.END)
        self.txtNoParkir.insert(tk.END, "")
        self.txtjeniskendaraan.delete(0, tk.END)
        self.txtjeniskendaraan.insert(tk.END, "")       
        self.txtjammasuk.delete(0, tk.END)
        self.txtjammasuk.insert(tk.END, "")
        self.txtjamkeluar.insert(0, tk.END)
        self.txtjamkeluar.insert(tk.END, "")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data rincian
        mk = Rincian()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        subjects = []
        for row_data in result:
            subjects.append(row_data)

        for subject in subjects:
            self.tree.insert('', tk.END, values=subject)
    
    def onCari(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = Rincian()
        res = mk.getByKodeMk(kodemk)
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNamaMK.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = Rincian()
        res = mk.getByKodeMk(kodemk)
        self.txtNamaMK.delete(0, tk.END)
        self.txtNamaMK.insert(tk.END, mk.namamk)
        self.txtSKS.delete(0, tk.END)
        self.txtSKS.insert(tk.END, mk.sks)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtKodeMK.get()
        namamk = self.txtNamaMK.get()
        sks = self.txtSKS.get()
        
        mk = Rincian()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if self.ditemukan:
            res = mk.updateByKodeMk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = Rincian()
        mk.kodemk = kodemk
        if self.ditemukan:
            res = mk.deleteByKodeMk(kodemk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormRincian(root, "Aplikasi Data Rincian")
    root.mainloop()