# Detection Tips

Detecting sophisticated spyware requires cross-referencing process states and monitoring system anomalies.

### Critical Indicators of Compromise (IoCs)
1. **Unsigned Driver Objects**: Check for newly loaded kernel objects that lack standard cryptographic certification from major OS providers.
2. **Persistent Raw Input Hooks**: Monitor software calls to APIs like `SetWindowsHookEx` or `RegisterRawInputDevices` without a corresponding UI context.
3. **Outbound Data Anomalies**: Audit background data transmissions to unknown external IP addresses, especially during periods of system inactivity.