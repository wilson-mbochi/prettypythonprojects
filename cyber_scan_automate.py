print ("\n----------- We're going to conduct the following tasks: ----------- \n"
       "1. Scan hosts on a network by ip or domain name using python-nmap module \n"
       "2. Identify the hosts with most open ports and services using -sV option \n"
       "3. Run a vulnerability scan on it using nmap vuln script \n"
       "4. Pull the logs of the machine using wmi module \n"
       "5. Analyze the logs for any suspicious processes using regular expressions module \n"
       "-------------------------------------------------------------------- \n")

print("Please download and install the following Python package modules before running script:\n"
      "1. 'pip install nmap' - for running network and vulnerability scans \n"
      "2. 'pip install wmi' - for pulling logs for local or remote Windows hosts\n")


userName = input("Enter your name to acknowledge you will not run this script on networks/machines without explicit permission: ")
print("Thank you ",userName,"..You deserve a donut! :) \n")

print("\n\n-----------Script Task 1 & 2 underway...Recon time!-----------\n"
      "--------------------------------------------------------------")

import nmap

def scan_network(target):
    try:
        # Initialize the port scanner
        nm = nmap.PortScanner()

        # Perform a scan with service detection (-sV)
        nm.scan(hosts=target, arguments='-sV')

        # Dictionary to hold the host and the count of open ports
        host_ports_count = {}

        # Iterate over all hosts found
        for host in nm.all_hosts():
            print(f'Host: {host} ({nm[host].hostname()})')
            print(f'State: {nm[host].state()}')

            open_ports_count = 0

            # Check if host has open ports and list the services
            if 'tcp' in nm[host]:
                print("Open Ports and Running Services:")
                for port in nm[host]['tcp']:
                    port_state = nm[host]['tcp'][port]['state']
                    service_name = nm[host]['tcp'][port]['name']
                    service_version = nm[host]['tcp'][port].get('version', '')
                    product = nm[host]['tcp'][port].get('product', '')
                    extra_info = nm[host]['tcp'][port].get('extrainfo', '')

                    print(f'Port: {port}\tState: {port_state}\tService: {service_name}\tVersion: {service_version}\tProduct: {product}\tInfo: {extra_info}')
                    
                    # Increment the open ports count for this host
                    open_ports_count += 1

            # Store the count of open ports for each host
            host_ports_count[host] = open_ports_count
            print("\n")

        print("Scan complete.")

        # Sort the hosts by the number of open ports in descending order
        sorted_hosts = sorted(host_ports_count.items(), key=lambda x: x[1], reverse=True)

        # Display the top 3 hosts with the most open ports
        print("Top 3 Hosts with the Most Open Ports:")
        for host, count in sorted_hosts[:3]:
            print(f'Host: {host} ({nm[host].hostname()}) - Open Ports: {count}')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the target (subnet IP or domain name)
    target = input("Enter the subnet IP or domain name to scan:")
    print("Running a network scan on",target,"...")
    # Run the network scan
    scan_network(target)

print("\n\n-----------------------On to Task 3: Running vulnerability scans.-----------------------\n"
      "----------------------------------------------------------------------------------------")

def vulnerability_scan(target):
    try:
        # Re-initialize the nmap.PortScanner object
        nm = nmap.PortScanner()

        # Perform a vulnerability scan using NSE scripts on the specified host
        print(f"Running vulnerability scan on {target}...")
        nm.scan(hosts=target, arguments='--script vuln')

        # Check if the host has vulnerabilities
        if 'hostscript' in nm[target]:
            print("Vulnerability Scan Results:")
            for script in nm[target]['hostscript']:
                print(f'Script: {script["id"]}')
                print(f'Output:\n{script["output"]}\n')
        else:
            print("No vulnerabilities found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        target = input("Enter IP address or domain name to perform a vulnerability scan (or type 'exit' to quit): ")
        
        # Check if the user wants to exit the loop
        if target.lower() == 'exit':
            print("Exiting the vulnerability scanner.")
            break
        
        # Run the vulnerability scan
        vulnerability_scan(target)

print("\n\n-----------------------On to Task 4: Pulling logs of a local or remote Windows machine!-----------------------"
      "\n--------------------------------------------------------------------------------------------------------------\n")

import wmi
import datetime

def get_critical_events(host):
    try:
        # Connect to the WMI service on the remote or local host
        connection = wmi.WMI(computer=host)

        # Define the time range for the last 24 hours
        time_limit = datetime.datetime.now() - datetime.timedelta(days=1)
        time_limit_str = time_limit.strftime("%Y%m%d%H%M%S.000000-000")

        print("Query the Windows Event Log for 'SYSTEM' critical events in the last 24 hours. \nCan change script to 'Application' or 'Setup' or 'Security' \nCan change to 1 for Critical Error; 2 for Warning; 3 for Information; 4 for Security Audit Success; 5 for Security Audit Failure;")

        query = f"SELECT * FROM Win32_NTLogEvent WHERE Logfile = 'System' AND EventType = 1 AND TimeGenerated >= '{time_limit_str}'"
        events = connection.query(query)

        # Process and display up to 10 critical events
        if events:
            print(f"Found {len(events)} critical events in the last 24 hours on {host}. Displaying up to 10 events:\n")
            for i, event in enumerate(events[:10]):
                print(f"Event {i + 1}:")
                print(f"  Event ID: {event.EventCode}")
                print(f"  Source: {event.SourceName}")
                print(f"  Time Generated: {event.TimeGenerated}")
                print(f"  Message: {event.Message}\n")
        else:
            print(f"No critical events found in the last 24 hours on {host}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the target IP address or hostname
    target_host = input("Enter the IP address or hostname to retrieve critical events from: ")
    
    # Retrieve and display critical events
    get_critical_events(target_host)
    
print("\n\n-----------------------Task 5: Provide a full log file (txt format) to analyze for security risks!-----------------------\n"
      "-------------------------------------------------------------------------------------------------------------------------\n")

import re

def analyze_log(file_path):
    #Initialize report variable where we'll store details
    report = ""
    try:
        with open(file_path, 'r') as log_file:
            logs = log_file.readlines()

        # Counters for different security-related events
        failed_logins = 0
        successful_logins = 0
        errors = 0
        suspicious_activities = 0
        suspicious_lines = []

        # Regular expressions for common security events
        failed_login_pattern = re.compile(r'An Error occured during Logon|authentication failure|invalid user', re.IGNORECASE)
        successful_login_pattern = re.compile(r'successfully logged on|authentication succeeded', re.IGNORECASE)
        error_pattern = re.compile(r'error|fail|denied', re.IGNORECASE)
        suspicious_activity_pattern = re.compile(r'Auditing settings on object were changed|A logon was attempted using explicit credentials|local group membership was enumerated|attack', re.IGNORECASE)

        # Real-time feedback and report building
        print("Analyzing log file...")
        report += "Analyzing log file...\n"

        for line in logs:
            if failed_login_pattern.search(line):
                failed_logins += 1
            elif successful_login_pattern.search(line):
                successful_logins += 1
            elif error_pattern.search(line):
                errors += 1
            elif suspicious_activity_pattern.search(line):
                suspicious_activities += 1
                suspicious_lines.append(line.strip())

        # Build the report
        summary = (f"\nLog Analysis Summary for {file_path}:\n\n"
                   f"Total lines analyzed: {len(logs)}\n"
                   f"Failed login attempts: {failed_logins}\n"
                   f"Successful logins: {successful_logins}\n"
                   f"Errors entries found: {errors}\n"
                   f"Suspicious activities detected: {suspicious_activities}\n")
        print(summary)
        report += summary

        if suspicious_activities > 0:
            details = "Suspicious activity details:\n"
            #print(details)
            report += details
            for i, line in enumerate(suspicious_lines, start=1):
                detail_line = f"{i}. {line}\n"
                #print(detail_line)
                report += detail_line
        else:
            print("No suspicious activities detected.\n")
            report += "No suspicious activities detected.\n"
    
    except FileNotFoundError:
        error_message = f"File not found: {file_path}\n"
        print(error_message)
        report += error_message
    except Exception as e:
        error_message = f"An error occurred: {e}\n"
        print(error_message)
        report += error_message

    return report  # Return the report variable

if __name__ == "__main__":
    # Ask the user for the path to the log file
    log_file_path = input("Enter the path to the log file (in .txt format): ")
    
    # Analyze the log file and store the result in the report variable
    report = analyze_log(log_file_path)
        
    # Get the file path from the user
    save_path = input("Enter the file path where you want to save the report: ")
    with open(save_path, 'w') as file:
        file.write(report)
    print("Report saved! \nRefer to your log file as well for event details using the keywords matched from the script!")

#Generate report date
from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Format the date (e.g., YYYY-MM-DD format)
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

# Print completion message
print("\nReport completed on",formatted_date)
print("-----------------------The script has finished! Thank you",userName,"!-----------------------")



