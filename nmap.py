import nmap

def run_nmap_scan(hosts, ports, arguments, use_sudo):
    scanner = nmap.PortScanner()
    scan_result = scanner.scan(hosts=hosts, ports=ports, arguments=arguments, sudo=use_sudo)

    print("\n---------------- Scan Results ----------------")
    for host, host_info in scan_result['scan'].items():
        print("------------------------------------")
        print(f"Host: {host}")
        print(f"State: {host_info['status']['state']}")
        for proto, proto_info in host_info.items():
            if proto == 'tcp':
                for port, port_info in proto_info.items():
                    print(f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}")

def main():
    print("-------------nmap Scanner-------------")

    target = input("Host/IP: ").strip()
    ports = input("Port(s): ").strip()
    arguments = input("nmap arguments (-sn, -SP): ").strip()
    use_sudo = input("¿Ejecutar como super usuario?(y/n): ").strip().lower() in ["y", "yes"]

    try:
        ports = ",".join([p.strip() for p in ports.split(',')])
        run_nmap_scan(target, ports, arguments, use_sudo)
    except nmap.PortScannerError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
