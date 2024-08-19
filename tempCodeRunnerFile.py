for linha in self.matriz:
            print(" | ".join(str(num) if num != 0 else " " for num in linha))
            print("-" * 11)