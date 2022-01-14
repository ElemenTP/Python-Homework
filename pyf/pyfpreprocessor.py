import numpy as np

if __name__ == "__main__":
    optdata = np.zeros([900, 1800], dtype=np.float64)
    for v in range(8):
        isuffix = v // 4
        jsuffix = v % 4
        grid = np.loadtxt(
            f"data\\gpw_v4_population_count_rev11_2020_30_sec_{v+1}.asc", skiprows=6
        )
        for i in range(450):
            for j in range(450):
                value = np.float64(0.0)
                for m in range(24):
                    for n in range(24):
                        tmp = grid[i * 24 + m, j * 24 + n]
                        if tmp > 0.0:
                            value += tmp
                optdata[899 - (isuffix * 450 + i), jsuffix * 450 + j] = value
    np.savetxt("datagrid.asc", optdata, fmt="%.8e")
