import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import webbrowser

class ThreatGraphInspector:
    def __init__(self, root):
        self.root = root
        self.root.title("ThreatGraph Inspector")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e1e")
        
        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#1e1e1e")
        self.style.configure("TLabel", background="#1e1e1e", foreground="white")
        self.style.configure("TButton", background="#2e2e2e", foreground="white")
        self.style.map("TButton", background=[("active", "#3e3e3e")])
        self.style.configure("Treeview", background="#2e2e2e", foreground="white", fieldbackground="#2e2e2e")
        self.style.map("Treeview", background=[("selected", "#4e4e4e")])
        
        # Create main frames
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.left_panel = ttk.Frame(self.main_frame, width=200)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Navigation panel
        self.nav_label = ttk.Label(self.left_panel, text="Navigation", font=("Helvetica", 12, "bold"))
        self.nav_label.pack(pady=10)
        
        # Navigation buttons
        button_options = {"width": 20, "style": "TButton"}
        
        self.file_btn = ttk.Button(self.left_panel, text="Open Files", command=self.open_files, **button_options)
        self.file_btn.pack(pady=5)
        
        self.scan_btn = ttk.Button(self.left_panel, text="Scan for Threats", command=self.scan_threats, **button_options)
        self.scan_btn.pack(pady=5)
        
        self.graph_btn = ttk.Button(self.left_panel, text="Dependency Graph", command=self.show_dependency_graph, **button_options)
        self.graph_btn.pack(pady=5)
        
        self.dashboard_btn = ttk.Button(self.left_panel, text="Risk Dashboard", command=self.show_risk_dashboard, **button_options)
        self.dashboard_btn.pack(pady=5)
        
        self.export_btn = ttk.Button(self.left_panel, text="Export Report", command=self.export_report, **button_options)
        self.export_btn.pack(pady=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview for file explorer
        self.tree_frame = ttk.Frame(self.right_panel)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("type", "path"), show="tree")
        self.tree.heading("#0", text="Files", anchor=tk.W)
        self.tree.column("#0", width=300)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Add context menu
        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(label="View Details", command=self.view_file_details)
        self.context_menu.add_command(label="Visual Diff", command=self.show_visual_diff)
        self.tree.bind("<Button-3>", self.show_context_menu)
        
        # Results tabs
        self.notebook = ttk.Notebook(self.right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.vuln_tab = ttk.Frame(self.notebook)
        self.config_tab = ttk.Frame(self.notebook)
        self.secrets_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.vuln_tab, text="Vulnerabilities")
        self.notebook.add(self.config_tab, text="Misconfigurations")
        self.notebook.add(self.secrets_tab, text="Secrets")
        
        # Initialize dummy data (replace with actual scan results)
        self.tree.insert("", "end", text="sample_code.py", values=("file", "sample_code.py"))
        self.tree.insert("", "end", text="config.json", values=("file", "config.json"))
        
    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
        
    def open_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Files to Analyze",
            filetypes=[("All Files", "*"), ("Python Files", "*.py"), ("Config Files", "*.json *.yaml *.toml"), ("Text Files", "*.txt")]
        )
        if file_paths:
            self.tree.delete(*self.tree.get_children())
            for path in file_paths:
                file_name = path.split("/")[-1]
                self.tree.insert("", "end", text=file_name, values=("file", path))
            self.status_var.set(f"Loaded {len(file_paths)} files for analysis")
        
    def scan_threats(self):
        if not self.tree.get_children():
            messagebox.showwarning("No Files", "Please load files first")
            return
            
        self.status_var.set("Scanning for threats...")
        self.root.update()
        
        # Mock scan results (replace with actual scanning logic)
        vulnerabilities = [
            {"type": "CVE", "id": "CVE-2023-1234", "severity": "High", "file": "sample_code.py", "line": 42, "description": "XXE vulnerability"},
            {"type": "CVE", "id": "CVE-2023-5678", "severity": "Medium", "file": "sample_code.py", "line": 87, "description": "SQL injection"}
        ]
        
        misconfigurations = [
            {"type": "Misconfig", "id": "AWS-001", "severity": "Critical", "file": "config.json", "line": 3, "description": "S3 bucket policy too permissive"},
            {"type": "Misconfig", "id": "K8S-002", "severity": "Medium", "file": "config.json", "line": 12, "description": "Missing resource limits"}
        ]
        
        secrets = [
            {"type": "Secret", "id": "AWS_KEY", "severity": "High", "file": "sample_code.py", "line": 10, "description": "AWS access key in code"},
            {"type": "Secret", "id": "DB_PWD", "severity": "Critical", "file": "sample_code.py", "line": 15, "description": "Database password exposure"}
        ]
        
        self.populate_vuln_tab(vulnerabilities)
        self.populate_config_tab(misconfigurations)
        self.populate_secrets_tab(secrets)
        
        self.status_var.set("Scan completed. Found:" 
                          f" {len(vulnerabilities)} vulnerabilities, "
                          f"{len(misconfigurations)} misconfigurations, "
                          f"{len(secrets)} secrets.")
    
    def populate_vuln_tab(self, vulnerabilities):
        # Clear existing widgets
        for widget in self.vuln_tab.winfo_children():
            widget.destroy()
            
        columns = ("ID", "Severity", "File", "Line", "Description")
        tree = ttk.Treeview(self.vuln_tab, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.W)
        
        for vuln in vulnerabilities:
            tree.insert("", "end", values=(
                vuln["id"],
                vuln["severity"],
                vuln["file"],
                vuln["line"],
                vuln["description"]
            ))
            
        scrollbar = ttk.Scrollbar(self.vuln_tab, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.vuln_tab.grid_rowconfigure(0, weight=1)
        self.vuln_tab.grid_columnconfigure(0, weight=1)
    
    def populate_config_tab(self, misconfigurations):
        for widget in self.config_tab.winfo_children():
            widget.destroy()
            
        columns = ("ID", "Severity", "File", "Line", "Description")
        tree = ttk.Treeview(self.config_tab, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.W)
        
        for config in misconfigurations:
            tree.insert("", "end", values=(
                config["id"],
                config["severity"],
                config["file"],
                config["line"],
                config["description"]
            ))
            
        scrollbar = ttk.Scrollbar(self.config_tab, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.config_tab.grid_rowconfigure(0, weight=1)
        self.config_tab.grid_columnconfigure(0, weight=1)
    
    def populate_secrets_tab(self, secrets):
        for widget in self.secrets_tab.winfo_children():
            widget.destroy()
            
        columns = ("ID", "Severity", "File", "Line", "Description")
        tree = ttk.Treeview(self.secrets_tab, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.W)
        
        for secret in secrets:
            tree.insert("", "end", values=(
                secret["id"],
                secret["severity"],
                secret["file"],
                secret["line"],
                secret["description"]
            ))
            
        scrollbar = ttk.Scrollbar(self.secrets_tab, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.secrets_tab.grid_rowconfigure(0, weight=1)
        self.secrets_tab.grid_columnconfigure(0, weight=1)
    
    def show_dependency_graph(self):
        messagebox.showinfo("Feature", "Dependency graph view would open here with package dependencies visualized")
        # In production, use pyvis, networkx, or graphviz for visualization
        
    def show_risk_dashboard(self):
        messagebox.showinfo("Feature", "Risk dashboard would display security metrics and trends here")
        # In production, use matplotlib, seaborn, or plotly for visualizations
    
    def export_report(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Report", "*.json"), ("All Files", "*")],
            title="Save Report As"
        )
        if file_path:
            # Mock report data (replace with actual report generation)
            report_data = {
                "summary": {
                    "vulnerabilities": 2,
                    "misconfigurations": 2,
                    "secrets": 2,
                    "critical": 2,
                    "high": 2,
                    "medium": 2
                },
                "details": {
                    "files": ["sample_code.py", "config.json"],
                    "timestamp": "2023-12-14T12:00:00Z"
                }
            }
            
            with open(file_path, "w") as f:
                json.dump(report_data, f, indent=2)
            
            self.status_var.set(f"Report saved to {file_path}")
    
    def view_file_details(self):
        selected = self.tree.selection()
        if not selected:
            return
            
        item = self.tree.item(selected[0])
        file_path = item["values"][1]
        
        # In production, show actual file content with highlighted issues
        messagebox.showinfo("File Details", f"Details for {file_path}")
    
    def show_visual_diff(self):
        selected = self.tree.selection()
        if not selected:
            return
            
        item = self.tree.item(selected[0])
        file_path = item["values"][1]
        
        # In production, implement diff visualization with difflib or similar
        messagebox.showinfo("Visual Diff", f"Visual diff for {file_path} would show here")

def main():
    root = tk.Tk()
    app = ThreatGraphInspector(root)
    root.mainloop()

if __name__ == "__main__":
    main()