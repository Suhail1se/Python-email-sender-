import wmi

def check_antivirus_status():
    # Connect to WMI
    c = wmi.WMI(namespace="root\SecurityCenter2")

    # Get antivirus products
    antiviruses = c.AntiVirusProduct()

    if not antiviruses:
        print("No antivirus product found.")
        return

    for av in antiviruses:
        print(f"Antivirus Name: {av.displayName}")
        print(f"Product State: {av.productState}")
        print("-" * 30)

if __name__ == "__main__":
    check_antivirus_status()
