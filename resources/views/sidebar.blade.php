<div class="sidebar bg-gray-800 text-white h-full min-h-screen p-5">
    <div class="sidebar-header mb-8 flex items-center justify-between">
        <h2 class="text-2xl font-bold">My App</h2>
        <button class="md:hidden text-gray-400 hover:text-white focus:outline-none" id="sidebarToggle">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
        </button>
    </div>
    <nav>
        <ul class="space-y-4">
            <li>
                <a href="{{ route('dashboard') }}"
                   class="flex items-center px-3 py-2 rounded hover:bg-gray-700 transition-colors duration-200
                   {{ request()->routeIs('dashboard') ? 'bg-gray-900' : '' }}">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                              d="M3 3h18v18H3V3z"/>
                    </svg>
                    Dashboard
                </a>
            </li>
            <li>
                <a href="{{ route('profile') }}"
                   class="flex items-center px-3 py-2 rounded hover:bg-gray-700 transition-colors duration-200
                   {{ request()->routeIs('profile') ? 'bg-gray-900' : '' }}">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                              d="M5.121 17.804A4 4 0 1116.88 6.195m-6.438 8.2a4 4 0 005.757-5.758"/>
                    </svg>
                    Profile
                </a>
            </li>
            <li>
                <a href="{{ route('settings') }}"
                   class="flex items-center px-3 py-2 rounded hover:bg-gray-700 transition-colors duration-200
                   {{ request()->routeIs('settings') ? 'bg-gray-900' : '' }}">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                              d="M12 8v4l3 3"/>
                        <circle cx="12" cy="12" r="10" stroke="none"/>
                    </svg>
                    Settings
                </a>
            </li>
            <li>
                <a href="{{ route('logout') }}"
                   onclick="event.preventDefault(); document.getElementById('logout-form').submit();"
                   class="flex items-center px-3 py-2 rounded hover:bg-red-600 transition-colors duration-200 text-red-400 hover:text-white">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                              d="M17 16l4-4m0 0l-4-4m4 4H7"/>
                    </svg>
                    Logout
                </a>
                <form id="logout-form" action="{{ route('logout') }}" method="POST" class="hidden">
                    @csrf
                </form>
            </li>
        </ul>
    </nav>
</div>

<script>
    document.getElementById('sidebarToggle').addEventListener('click', function () {
        const sidebar = this.closest('.sidebar');
        sidebar.classList.toggle('hidden');
    });
</script>