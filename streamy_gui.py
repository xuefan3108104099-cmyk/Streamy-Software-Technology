import tkinter as tk
from tkinter import ttk, scrolledtext
from streamy_core import TVShow, Film, Season, Episode, Actor, Genre, Review

class StreamyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Streamy Streaming Platform GUI")
        self.root.geometry("780x580")

        # 初始化样例业务数据
        self.sci_fi = Genre("Sci‑Fi")
        self.show = TVShow("Stranger Things",2016,"Netflix")
        s1 = Season(1)
        s1.add_episode(Episode("Chapter One",2880))
        self.show.add_season(s1)
        self.show.link_actor(Actor("Ashley Peacock"))
        self.show.add_review(5,"Very good show!")
        self.sci_fi.register_title(self.show)

        tab_control = ttk.Notebook(root)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="播放鉴权测试")
        tab_control.add(tab2, text="分类目录查看")
        tab_control.add(tab3, text="级联删除测试")
        tab_control.pack(expand=1, fill="both")

        # Tab1 播放鉴权
        ttk.Label(tab1, text="输入Access Token：").pack(pady=6)
        self.token_entry = ttk.Entry(tab1, width=65)
        self.token_entry.insert(0,"VALID_STREAM_TOKEN_2026")
        self.token_entry.pack()
        self.log_text = scrolledtext.ScrolledText(tab1,height=16)
        self.log_text.pack(padx=12,pady=10,fill="both",expand=True)
        ttk.Button(tab1,text="执行播放请求", command=self.test_play).pack(pady=4)

        # Tab2 分类目录
        ttk.Button(tab2, text="展示Genre媒体目录", command=self.show_catalog).pack(pady=10)
        self.catalog_text = scrolledtext.ScrolledText(tab2,height=22)
        self.catalog_text.pack(padx=12,pady=6,fill="both",expand=True)

        # Tab3 级联删除
        ttk.Button(tab3, text="触发TVShow级联清除", command=self.purge_gui).pack(pady=10)
        self.del_log = scrolledtext.ScrolledText(tab3,height=22)
        self.del_log.pack(padx=12,pady=6,fill="both",expand=True)

    def test_play(self):
        token = self.token_entry.get()
        self.log_text.delete(1.0, tk.END)
        import io, sys
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        self.show.play_media(token)
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        self.log_text.insert(tk.END, output)

    def show_catalog(self):
        import io, sys
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        self.sci_fi.display_catalog()
        out = new_stdout.getvalue()
        sys.stdout = old_stdout
        self.catalog_text.delete(1.0,tk.END)
        self.catalog_text.insert(tk.END, out)

    def purge_gui(self):
        import io, sys
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        self.show.purge_tv_show_data()
        out = new_stdout.getvalue()
        sys.stdout = old_stdout
        self.del_log.delete(1.0,tk.END)
        self.del_log.insert(tk.END, out)


if __name__ == "__main__":
    window = tk.Tk()
    app = StreamyGUI(window)
    window.mainloop()
