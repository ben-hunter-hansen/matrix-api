
from app.matrix import Matrix
from app import tests

def main():
    tests.run()
    A = Matrix.fromArray([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    B = Matrix.fromArray([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    print(A * B.transpose())


if __name__ == "__main__":
    main()
