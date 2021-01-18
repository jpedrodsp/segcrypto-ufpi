import asymmetric
import symmetric
import hashcalc
import utils
import json

TEST_REPEAT_LIST = [30, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000]

def test_asymmetric(repeats: int):
    text = utils.read_textcontent()
    rsa_publickey = utils.read_rsa_publickey()
    rsa_privatekey = utils.read_rsa_privatekey()
    
    # RSA Crypt
    crypt_times = []
    for time in range(0, repeats):
        ctime, cresult = asymmetric.crypt(text, rsa_publickey)
        crypt_times.append(ctime)
    crypt_average_time, crypt_total_time = utils.calculate_timeresult(crypt_times)
    
    # RSA Decrypt
    decrypt_times = []
    for time in range(0, repeats):
        dtime, dresult = asymmetric.decrypt(text, rsa_privatekey)
        decrypt_times.append(dtime)
    decrypt_average_time, decrypt_total_time = utils.calculate_timeresult(decrypt_times)

    print("Asymmetric Crypt Average Time ({}x): {} ms".format(repeats, crypt_average_time))
    print("Asymmetric Decrypt Average Time ({}x): {} ms".format(repeats, decrypt_average_time))
    print("Asymmetric Crypt Total Time ({}x): {} ms".format(repeats, crypt_total_time))
    print("Asymmetric Decrypt Total Time ({}x): {} ms".format(repeats, decrypt_total_time))
    return crypt_average_time, decrypt_average_time, crypt_total_time, decrypt_total_time

def test_symmetric(repeats: int):
    text = utils.read_textcontent()
    aeskey = utils.read_aes_key()
    
    # AES Crypt
    crypt_times = []
    for time in range(0, repeats):
        ctime, cresult = symmetric.crypt(text, aeskey)
        crypt_times.append(ctime)
    crypt_average_time, crypt_total_time = utils.calculate_timeresult(crypt_times)
    
    # AES Decrypt
    decrypt_times = []
    for time in range(0, repeats):
        dtime, dresult = symmetric.decrypt(text, aeskey)
        decrypt_times.append(dtime)
    decrypt_average_time, decrypt_total_time = utils.calculate_timeresult(decrypt_times)

    print("Symmetric Crypt Average Time ({}x): {} ms".format(repeats, crypt_average_time))
    print("Symmetric Decrypt Average Time ({}x): {} ms".format(repeats, decrypt_average_time))
    print("Symmetric Crypt Total Time ({}x): {} ms".format(repeats, crypt_total_time))
    print("Symmetric Decrypt Total Time ({}x): {} ms".format(repeats, decrypt_total_time))
    return crypt_average_time, decrypt_average_time, crypt_total_time, decrypt_total_time

def test_hashcalc(repeats: int):
    hash_times = []
    check_times = []
    for time in range(0, repeats):
        text = utils.read_textcontent()
        htime, hdata = hashcalc.hashtext(text)
        ctime, cresult = hashcalc.checkhash(text, hdata)
        if cresult == False:
            raise "Check result error - hashes doesn't match"
        hash_times.append(htime)
        check_times.append(ctime)
    hash_average_time, hash_total_time = utils.calculate_timeresult(hash_times)
    check_average_time, check_total_time = utils.calculate_timeresult(check_times)

    print("Hash-only Average Time ({}x): {} ms".format(repeats, hash_average_time))
    print("Hash with Check Average Time ({}x): {} ms".format(repeats, check_average_time))
    print("Hash-only Total Time ({}x): {} ms".format(repeats, hash_total_time))
    print("Hash with Check Total Time ({}x): {} ms".format(repeats, check_total_time))
    return hash_average_time, hash_total_time, check_average_time, check_total_time

if __name__ == "__main__":
    result = {}
    for testtimes in TEST_REPEAT_LIST:
        print("--- {}X times ---".format(testtimes))
        aca, ada, act, adt = test_asymmetric(testtimes)
        sca, sda, sct, sdt = test_symmetric(testtimes)
        hha, hca, hht, hct = test_hashcalc(testtimes)
        if "asymmetric" not in result:
            result["asymmetric"] = {}
        result["asymmetric"][testtimes] = (aca, ada, act, adt)
        if "symmetric" not in result:
            result["symmetric"] = {}
        result["symmetric"][testtimes] = (sca, sda, sct, sdt)
        if "hash" not in result:
            result["hash"] = {}
        result["hash"][testtimes] = (hha, hca, hht, hct)
    
    print(result)

    print("Saving result...")
    fp = open("result.txt", "w")
    json.dump(result, fp)
    fp.close()
    