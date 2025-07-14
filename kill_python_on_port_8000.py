import psutil


def find_python_using_port(port: int):
    matching_pids = set()
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            try:
                proc = psutil.Process(conn.pid)
                if proc.name().lower() == "python.exe":
                    matching_pids.add(proc.pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return matching_pids


def kill_python_on_port(port: int):
    pids = find_python_using_port(port)
    if not pids:
        print(f"✅ No python.exe processes found using port {port}.")
        return

    print(f"🔴 Attempting to kill python.exe processes using port {port}: {pids}")
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(timeout=5)
            print(f"✅ Killed python.exe with PID {pid}")
        except Exception as e:
            print(f"❌ Failed to kill PID {pid}: {e}")


if __name__ == "__main__":
    kill_python_on_port(8000)
