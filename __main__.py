
from app.matrix import Matrix

def main():
    A = Matrix.fromArray([
        [0,2,3],
        [4,2,6],
        [4,5,6]
    ])
    B = Matrix.fromArray([
        [4, 9, 6],
        [7, 8, 1],
        [0, 13,2]
    ])
    print(A - B)
    print(A.determinant())


if __name__ == "__main__":
    main()
