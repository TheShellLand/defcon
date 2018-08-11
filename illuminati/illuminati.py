import base64
import codecs


def rot13(input):
    s = input
    enc = codecs.getencoder("rot-13")
    os = enc(s)[0]

    return os


def invitation_card():
    key = b'aHR0cDovL2RjM' \
          b'jYubWluZXJ2YW' \
          b'xsdXguY29tL2N' \
          b'oYWxsZW5nZS8='
    key = base64.decodebytes(key).decode()
    print(key)
    # http://dc26.minervallux.com/challenge/

    unknown = '''Envgyva'f Punyyratr QP26\n''' \
              '''Rnpu lrne zlevnaqf pbzcrgr\n''' \
              '''sbe tybel. Bayl gur pyrire srj\n''' \
              '''svaq jung frperg yvrf orlbaq\n''' \
              '''gur nffrzoyntr bs ceboyrzf\n''' \
              '''Qrpbqr gur grkg orybj gb\n''' \
              '''ortva. Cebsbhaq ertneqf!\n'''
    message = rot13(unknown)
    # Raitlin's Challenge DC26
    # Each year myriands compete
    # for glory. Only the clever few
    # find what secret lies beyond
    # the assemblage of problems
    # Decode the text below to
    # begin. Profound regards!

    print(message)


def puzzle3():
    message = 'typing passwords\n' \
              'we are a bot slewed.\n' \
              'wutg iyr fubgersm\n' \
              'rypinf rhw xosw qeonf,\n' \
              'yhrtr id no stmot shsindy gsyr'

    unknown = 'wutg iyr fubgersm\n' \
              'rypinf rhw xosw qeonf,\n' \
              'yhrtr id no stmot shsindy gsyr'
    # not rot13

    print(rot13(unknown))
    print(message)


puzzle3()
