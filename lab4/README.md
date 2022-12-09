# Краткий обзор

Для построения GRE over IPSEC VPN тунеля я использовал аутентификацию с обменом ключей. На маршрутизаторе R1 поднимается 2 тунеля:
- Чистый GRE
- GRE over IPSEC

для каждого из них я сделал дополнительный статический маршрут во входящий виртуальный интерфейс тунеля, чтобы перенаправлять трафик на другой конец по нужному IP удаленной подсети.

# Ping GRE

![ping_gre](./images/ping_gre.png)


# Ping GRE over IPSEC

![ping_gre](./images/ping_gre_ipsec.png)

# IPSEC info

![ping_gre](./images/ipsec_info.png)

# Ping GRE over IPSEC Wireshark cast

![ping_gre](./images/ipsec_wireshark.png)

# Ping GRE Wireshark

![ping_gre](./images/gre_wireshark.png)
