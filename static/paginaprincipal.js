const toggleBtn = document.getElementById('toggle-btn');
const sidebar = document.getElementById('sidebar');
const content = document.getElementById('content');

toggleBtn.addEventListener('click', function () {
    sidebar.classList.toggle('hidden');
    content.classList.toggle('expanded');
});

// Alterna el submenú
function toggleSubMenu(submenuId) {
    const submenu = document.getElementById(submenuId);
    submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
}

// Resalta el elemento activo
document.querySelectorAll('.sidebar ul li a').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('.sidebar ul li').forEach(li => li.classList.remove('active'));
        this.parentElement.classList.add('active');
    });
});


  

// Alterna el menú lateral
document.getElementById('toggle-btn').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('active');
});

// Resalta el elemento activo
document.querySelectorAll('.sidebar ul li a').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('.sidebar ul li').forEach(li => li.classList.remove('active'));
        this.parentElement.classList.add('active');
    });
});


