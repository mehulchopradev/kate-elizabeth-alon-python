marks = [5, 6, 4, 5, 8, 8, 10, 9, 3, 6, 10, 6, 3, 7, 4, 10, 8]

# unique (distinct) set of marks
# list -> set

s = list(set(marks))
print(s)

ma = [1, 3, 5, 10, 9]
mb = [3, 4, 5, 2]

sma = set(ma)
smb = set(mb)

# common set of marks that was scored between the two divisions (intersection)
print(list(sma & smb))

# all the marks that was scored between the two divisions (union)
print(list(sma | smb))

# marks that were exclusively scored by division a
print(list(sma - smb))

# marks that were exclusively scored by division b
print(list(smb- sma))

# marks that were scored exclusively in division a or division b
print(list(sma ^ smb))