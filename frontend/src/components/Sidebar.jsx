export default function Sidebar({ darkMode, setDarkMode }) {
    const handleUpload = async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        await uploadPDF(file);
        alert("File uploaded!");
    };

    return (
        <div className="sidebar">
            <h1>📄 Upload PDF</h1>
            <input type="file" accept=".pdf" onChange={handleUpload} style={{ margin: "20px 0", }} />
            <div className="sidebar-footer" >
                Developed by @ <strong>Sumit Saurabh</strong>
            </div>

        </div>
    );

}
