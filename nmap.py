import nmap

def scan():
    # Interacción con el usuario para obtener la configuración de escaneo
    hosts = input("Ingrese los hosts a escanear (separados por coma): ").strip()
    ports = input("Ingrese los puertos a escanear (separados por coma o rango - ej. 80,443,1000-2000): ").strip()
    arguments = input("Ingrese argumentos adicionales para nmap (si es necesario): ").strip()
    use_sudo = input("¿Desea ejecutar como superusuario? (y/n): ").strip().lower() == 'y'
    
    # Configurar el escáner nmap
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, ports=ports, arguments=arguments, sudo=use_sudo)
    
    # Mostrar resultados del escaneo
    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    scan()

