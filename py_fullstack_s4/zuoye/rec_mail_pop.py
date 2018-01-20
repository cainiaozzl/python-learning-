#!/usr/bin/env python
#coding: cp936
#python_version: 2.7


import poplib
import email
import sys
import re


class SearchMail(object):
    # 用于标识是否找到指定内容的邮件
    search_flag = False

    #获取邮件方法
    @staticmethod
    def get_mail(host, user, password, search_key, port=110, ssl=False):
        """
        :param host: mail server ip address
        :param user: mail login user name
        :param password: mail login user's password
        :param search_key: search keys  实际这里是来自ftpin@7road.com和search_keys共同决定
        :param port: mail server connect port
        :param ssl: use ssl connection or not
        :return: return a tuple (a, b, c),
                    'a': a logic value, telling user search success or not
                    'b': a mail data or None
                    'c': a description for this searching
        """

        # 获得字符编码方法
        def get_charset(message, default="ascii"):
            charset = message.get_content_charset()
            return charset if charset else default

        # 定义解析邮件方法
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

        # search_key参数为空是， 直接返回None
        if not search_key:
            sys.stdout('没有传入搜索关键字参数!' + '\n')
            sys.exit(1)
            # raise Exception, 'error function call: search_key var is null'

        # 根据ssl设置， 建立不同的pop3连接
        if ssl == 1:
            pop3_conn = poplib.POP3_SSL(host, port)
        else:
            pop3_conn = poplib.POP3(host, port)

        pop3_conn.user(user)
        pop3_conn.pass_(password)

        total_number_mail = pop3_conn.stat()[0]
        
        for item in iter(pop3_conn.list()[1][-1::-1]):
            # 取得邮件序列号, 大小. 这里的大小是字节为单位
            number, size = item.split()
            sys.stdout.write('\r---------------- %d/%d ---------------' % (
                total_number_mail - int(number) + 1, total_number_mail))
            # 如果一封邮件大小超过 10k, 肯定不是OA发来的接受更新包的邮件, 跳过.
            if int(size) > 1024 * 10: continue

            lines = pop3_conn.retr(number)[1]
            # 取得加密的邮件内容
            msg = email.message_from_string('\n'.join(lines))

            # msg.get('From')
            # 第一个为发件人邮件别名, 第二个为真实发件人邮件地址
            # '"benny.liao@7road.com" <benny.liao@7road.com>'
            # from_info_tuple =  email.utils.parseaddr(msg.get('from'))
            # ('jiwei.qian', 'jiwei.qian@7road.com')
            from_address = email.utils.parseaddr(msg.get('from'))[1]

            if from_address in 'ftpin@7road.com':
                # str_date = 'Date : ' + msg["Date"]
                # subject = email.Header.decode_header(msg["Subject"])
                # sub = my_unicode(subject[0][0], subject[0][1])
                # str_sub = 'Subject : ' + sub

                # 处理邮件正文内容
                data = parse_email(msg)
                if ":" + search_key + "<" in data:
                    # 找到对应邮件后，设置找到标志位真, 立即退出，不再搜索
                    search_flag = True
                    receive_time = msg.get('Received').split(';')[1].strip()
                    break
            else:
                continue

        # 关闭pop3服务器连接
        pop3_conn.quit()

        sys.stdout.write('\n')
        if search_flag:
            return data, receive_time
        else:
            # raise Exception, 'cat not find any matched mail'
            sys.stdout.wirte('无法从收件箱中找到相匹配的邮件!' + '\n')
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
        sys.stdout.write('请传入一个参数以用作搜索邮件内容的关键字!' + '\n')
        sys.exit(1)
        # raise Exception, 'do not call script with an argument!'

    # 开始搜索邮件前, 先把之前记录邮件内容的文件先清空!
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
