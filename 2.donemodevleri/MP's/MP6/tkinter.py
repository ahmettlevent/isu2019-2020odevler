from tkinter import *
class Analiz(Frame):
    def init(self, parent):
        Frame.init(self, parent)
        self.parent = parent
        self.var = StringVar()
        self.inituI()

    def inituI(self):
        #Programın arayüzünü oluşturduk
        Label(self.parent, bg="misty rose", text="İstinye Ders Analizcisi").grid(row = 0, column = 2, padx = 0,ipadx=0,ipady=0)

        Label(self.parent, bg="misty rose", text="Benzerlik Ölçütü").grid(row=3, column=0,padx=0,ipady=0)

        Label(self.parent, bg="misty rose", text="Ders Kodu Örnekleri").grid(row=2, column=4, padx=0,ipady=0)

        Listbox(self.parent, bg="misty rose").grid(row=2, column=5, padx=0, ipady=0,sticky=W)

        Button(self.parent, bg="misty rose", text="Hiyeraşik Kümeleri Göster").grid(row=4, column=1, padx=0, ipady=0,pady=40)

        Button(self.parent, bg="misty rose", text="Veri Matrisini Göster").grid(row=4, column=3, padx=0, ipady=0,pady=0)

        Button(self.parent, bg="misty rose", text="Veri Setini Yükle").grid(row=1, column=1, padx=0, ipady=0,pady=0)

        Text(self.parent,width=95,height=25).grid(row=5,column=0,sticky=W,ipadx=0,ipady=0,columnspan=6)



        R1 = Radiobutton(self.parent, text="Pearson", variable=self.var, value="Pearson",command="")
        R1.grid(row=3,column=1)

        R2 = Radiobutton(self.parent, text="Tanimoto", variable=self.var, value="Tanimato",command="")
        R2.grid(row=4,column=1,sticky=N)

#Programın çalışması için gerekli fonksiyonu yazdık
def main():
    root = Tk()
    root.geometry("1000x800+485+55")
    root.resizable(width=FALSE, height=FALSE)
    root.configure(bg="black")
    app = Analiz(root)
    root.mainloop()


main()