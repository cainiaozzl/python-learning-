#!/usr/bin/env python
#coding: cp936
#python_version: 2.7


import poplib
import email
import sys
import re


class SearchMail(object):
    # ���ڱ�ʶ�Ƿ��ҵ�ָ�����ݵ��ʼ�
    search_flag = False

    #��ȡ�ʼ�����
    @staticmethod
    def get_mail(host, user, password, search_key, port=110, ssl=False):
        """
        :param host: mail server ip address
        :param user: mail login user name
        :param password: mail login user's password
        :param search_key: search keys  ʵ������������ftpin@7road.com��search_keys��ͬ����
        :param port: mail server connect port
        :param ssl: use ssl connection or not
        :return: return a tuple (a, b, c),
                    'a': a logic value, telling user search success or not
                    'b': a mail data or None
                    'c': a description for this searching
        """

        # ����ַ����뷽��
        def get_charset(message, default="ascii"):
            charset = message.get_content_charset()
            return charset if charset else default

        # ��������ʼ�����
        def parse_email(msg):
            # content_list = []
            for part in msg.walk():
                if not part.is_multipart():
                    #content_type = part.get_content_type()
                    charset = get_charset(part)

                    #if content_type in ['text/plain']:
                    #    suffix = '.txt'
                    #if content_type in ['text/html']:
                    #    suffix = '.htm'
                    if charset == None:
                        data = part.get_payload(decode=True).encode('utf-8')
                    else:
                        data = part.get_payload(decode=True).decode(charset).encode('utf-8')
                        # content_list.append((suffix, data))
            # return  content_list
            return data

        # search_key����Ϊ���ǣ� ֱ�ӷ���None
        if not search_key:
            sys.stdout('û�д��������ؼ��ֲ���!' + '\n')
            sys.exit(1)
            # raise Exception, 'error function call: search_key var is null'

        # ����ssl���ã� ������ͬ��pop3����
        if ssl == 1:
            pop3_conn = poplib.POP3_SSL(host, port)
        else:
            pop3_conn = poplib.POP3(host, port)

        pop3_conn.user(user)
        pop3_conn.pass_(password)

        total_number_mail = pop3_conn.stat()[0]
        
        for item in iter(pop3_conn.list()[1][-1::-1]):
            # ȡ���ʼ����к�, ��С. ����Ĵ�С���ֽ�Ϊ��λ
            number, size = item.split()
            sys.stdout.write('\r---------------- %d/%d ---------------' % (
                total_number_mail - int(number) + 1, total_number_mail))
            # ���һ���ʼ���С���� 10k, �϶�����OA�����Ľ��ܸ��°����ʼ�, ����.
            if int(size) > 1024 * 10: continue

            lines = pop3_conn.retr(number)[1]
            # ȡ�ü��ܵ��ʼ�����
            msg = email.message_from_string('\n'.join(lines))

            # msg.get('From')
            # ��һ��Ϊ�������ʼ�����, �ڶ���Ϊ��ʵ�������ʼ���ַ
            # '"benny.liao@7road.com" <benny.liao@7road.com>'
            # from_info_tuple =  email.utils.parseaddr(msg.get('from'))
            # ('jiwei.qian', 'jiwei.qian@7road.com')
            from_address = email.utils.parseaddr(msg.get('from'))[1]

            if from_address in 'ftpin@7road.com':
                # str_date = 'Date : ' + msg["Date"]
                # subject = email.Header.decode_header(msg["Subject"])
                # sub = my_unicode(subject[0][0], subject[0][1])
                # str_sub = 'Subject : ' + sub

                # �����ʼ���������
                data = parse_email(msg)
                if ":" + search_key + "<" in data:
                    # �ҵ���Ӧ�ʼ��������ҵ���־λ��, �����˳�����������
                    search_flag = True
                    receive_time = msg.get('Received').split(';')[1].strip()
                    break
            else:
                continue

        # �ر�pop3����������
        pop3_conn.quit()

        sys.stdout.write('\n')
        if search_flag:
            return data, receive_time
        else:
            # raise Exception, 'cat not find any matched mail'
            sys.stdout.wirte('�޷����ռ������ҵ���ƥ����ʼ�!' + '\n')
            sys.exit(1)


if __name__ == '__main__':
    __month_dict = {
                'Apr': '04',
                'Aug': '08',
                'Dec': '12',
                'Feb': '02',
                'Jan': '01',
                'Jul': '07',
                'Jun': '06',
                'Mar': '03',
                'May': '05',
                'Nov': '11',
                'Oct': '10',
                'Sep': '09',
                }

    host = 'mail.7road.com'
    user = 'zilin.zeng'
    password = 'a123456!'
    file_name = 'mail_content'

    if len(sys.argv) < 2:
        sys.stdout.write('�봫��һ�����������������ʼ����ݵĹؼ���!' + '\n')
        sys.exit(1)
        # raise Exception, 'do not call script with an argument!'

    # ��ʼ�����ʼ�ǰ, �Ȱ�֮ǰ��¼�ʼ����ݵ��ļ������!
    _content = open(file_name, 'wb')
    _content.truncate()
    _content.close()


    search_key = sys.argv[1]
    mail_content, _receive_time = SearchMail.get_mail(host, user, password, search_key)
    for ele in __month_dict.keys():
        if re.search(ele, _receive_time, flags=re.I):
            receive_time = re.sub(ele, __month_dict.get(ele), _receive_time, flags=re.I)


    with open(file_name, 'wb') as _content:
        _content.write('receive_time: %s\n' % receive_time)
        _content.write(mail_content + '\n')
