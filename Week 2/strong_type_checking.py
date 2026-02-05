x = "10"
y = 5

# Python does NOT auto-convert types
result = x + y    # ❌ TypeError

#We have to convert the data types manually for it to work
result = int(x) + y   # ✅ Explicit conversion
print(result)