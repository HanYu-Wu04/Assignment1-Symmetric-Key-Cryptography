import matplotlib.pyplot as plt

# AES Data
block_sizes_aes = [16, 64, 256, 1024, 8192, 16384]

aes_128_throughput = [1099376.37, 1432314.52, 1556384.54, 1589946.37, 1601328.47, 1590039.17]
aes_192_throughput = [1032655.82, 1226000.90, 1294314.92, 1312945.49, 1316042.07, 1323449.11]
aes_256_throughput = [858771.39, 1063301.87, 1113648.64, 1130881.97, 1136359.60, 1139501.74]

# Plotting the AES graph
plt.figure(figsize=(10, 6))
plt.style.use('seaborn-darkgrid')
plt.plot(block_sizes_aes, aes_128_throughput, label='AES-128-CBC', marker='o')
plt.plot(block_sizes_aes, aes_192_throughput, label='AES-192-CBC', marker='o')
plt.plot(block_sizes_aes, aes_256_throughput, label='AES-256-CBC', marker='o')

plt.xlabel('Block Size (bytes)')
plt.ylabel('Throughput (KBytes/s)')
plt.title('AES Performance Comparison')
plt.legend()
plt.grid(True)

plt.savefig('aes_performance_comparison_modified.png')

# RSA Data
rsa_key_sizes = [512, 1024, 2048, 3072, 4096, 7680, 15360]
rsa_sign_throughput = [53377.7, 11250.1, 1804.8, 624.7, 285.5, 34.7, 6.5]
rsa_verify_throughput = [546460.2, 231403.1, 72687.4, 34196.6, 19850.8, 5781.7, 1462.0]

# Plotting the RSA graph
plt.figure(figsize=(10, 6))
plt.style.use('ggplot')
plt.plot(rsa_key_sizes, rsa_sign_throughput, label='RSA Sign', marker='o')
plt.plot(rsa_key_sizes, rsa_verify_throughput, label='RSA Verify', marker='o')

plt.xlabel('RSA Key Size (bits)')
plt.ylabel('Throughput (operations per second)')
plt.title('RSA Performance Comparison')
plt.legend()
plt.grid(True)

plt.savefig('rsa_performance_comparison_modified.png')

plt.show()