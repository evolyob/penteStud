```py
Path = \home\tmp
FileName = oMyGost.sh
Algorithm = md5, sha1, sha256, sha512
# linux
md5sum %Path %FileName
sha1sum %Path\*

# Windows cmd
certutil -hashfile %Path %FileName %Algorithm

# Windows PowerShell
Get-FileHash %Path %FileName -algorithm %Algorithm | format-list
Get-FileHash %Path\* -algorithm %Algorithm | format-list
```
### dc3dd
```py
 fdisk-1

```
