def tgt(so):
    ket_qua = 1
    for i in range(2, so + 1):
        ket_qua *= i
    return ket_qua

def ctc():
    try:
        gt = int(input("Nhập một số nguyên dương: "))
        if gt < 0:
            print("Số nhập vào phải không âm. Vui lòng thử lại!")
        else:
            print(f"Kết quả: {gt}! = {tgt(gt)}")
    except ValueError:
        print("Lỗi! Hãy nhập vào một số nguyên hợp lệ.")

if __name__ == "__main__":
    ctc()
