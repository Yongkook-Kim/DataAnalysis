{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "실습.py",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "xWYdz2K53z53",
        "outputId": "59b14d15-1c26-4e9a-ec00-5b004e489d04"
      },
      "source": [
        "!pip install pymysql > /dev/null\n",
        "\n",
        "from google.colab import files\n",
        "uploaded = files.upload()\n",
        "filename = list(uploaded.keys())[0]"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-417f8ee8-8424-48d8-abf8-30f88321a2e9\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-417f8ee8-8424-48d8-abf8-30f88321a2e9\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "text": [
            "Saving mysql.json to mysql.json\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ju45kkNW3-4c"
      },
      "source": [
        "import json\n",
        "with open(filename) as fp:\n",
        "    config_str = fp.read()\n",
        "config = json.loads(config_str)"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0XU1QinH4CIB"
      },
      "source": [
        "import pymysql\n",
        "conn = pymysql.connect(\n",
        "    host=config['host'], \n",
        "    user=config['user'], \n",
        "    password=config['password'], \n",
        "    database=config['database'], \n",
        "    port=config['port']\n",
        ")"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qfGrSBIP4PFq"
      },
      "source": [
        "cur = conn.cursor()\n",
        "sql_products = '''\n",
        "create table if not exists products(\n",
        "    pid varchar(20) not null primary key,\n",
        "    pname varchar(20) not null,\n",
        "    pprice int default 0,\n",
        "    pcategory varchar(20),\n",
        "    pcost int default 0\n",
        ");\n",
        "'''"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7xXnAiC3705S"
      },
      "source": [
        "sql_sales = '''\n",
        "create table if not exists sales(\n",
        "    sid int primary key auto_increment,\n",
        "    sdate datetime default current_timestamp,\n",
        "    scompany varchar(20),\n",
        "    spid varchar(20),\n",
        "    sunit int default 0\n",
        ");\n",
        "'''"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m8V8te3Z8XBk",
        "outputId": "d368b7e9-73ea-471f-820f-cb6421d5acfd"
      },
      "source": [
        "cur.execute(sql_products)\n",
        "cur.execute(sql_sales)"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n-Fvnt3N8gSf"
      },
      "source": [
        "def data_add2products(pid1, pname1, pprice1, pcategory1, pcost1):\n",
        "    cur = conn.cursor()\n",
        "    sql_add = '''\n",
        "    insert into products(pid, pname, pprice, pcategory, pcost)\n",
        "    values (%s, %s, %s, %s, %s)'''\n",
        "    cur.execute(sql_add, (pid1, pname1, pprice1, pcategory1, pcost1))\n",
        "    conn.commit()"
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "57LbP08K-uVl"
      },
      "source": [
        "def data_add2sales(sdate1, scompany1, spid1, sunit1):\n",
        "    cur = conn.cursor()\n",
        "    sql_add = '''\n",
        "    insert into sales(sdate, scompany, spid, sunit)\n",
        "    values(%s, %s, %s, %s)'''\n",
        "    cur.execute(sql_add, (sdate1, scompany1, spid1, sunit1))\n",
        "    conn.commit()"
      ],
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RHaEkUHEA-A7"
      },
      "source": [
        "# 상품 추가\n",
        "data_add2products(100, '농구화', 120000, '신발', 60000)\n",
        "data_add2products(101, '탁구화', 150000, '신발', 100000)\n",
        "data_add2products(102, '축구화', 220000, '신발', 150000)\n",
        "data_add2products(103, '배구화', 80000, '신발', 60000)\n",
        "data_add2products(104, '볼링화', 95000, '신발', 65000)\n",
        "data_add2products(105, '테니스화', 139000, '신발', 110000)\n",
        "data_add2products(106, '골프화', 267000, '신발', 180000)\n",
        "data_add2products(107, '런닝화', 118000, '신발', 180000)\n",
        "data_add2products(108, '야구화', 193000, '신발', 177000)\n",
        "data_add2products(109, '펜싱화', 136000, '신발', 98000)\n",
        "data_add2products(110, '풋살화', 105000, '신발', 86000)\n",
        "data_add2products(111, '배드민턴화', 149000, '신발', 111000)\n",
        "data_add2products(112, '스쿼시화', 67000, '신발', 50000)"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NLSf04ESB_Kx"
      },
      "source": [
        "data_add2products(200, '농구바지', 12000, '바지', 6000)\n",
        "data_add2products(201, '탁구바지', 15000, '바지', 10000)\n",
        "data_add2products(202, '축구바지', 22000, '바지', 15000)\n",
        "data_add2products(203, '배구바지', 8000, '바지', 6000)\n",
        "data_add2products(204, '볼링바지', 9500, '바지', 6500)\n",
        "data_add2products(205, '테니스바지', 13900, '바지', 11000)\n",
        "data_add2products(206, '골프바지', 26700, '바지', 18000)\n",
        "data_add2products(207, '런닝바지', 11800, '바지', 18000)\n",
        "data_add2products(208, '야구바지', 19300, '바지', 17700)\n",
        "data_add2products(209, '펜싱바지', 13600, '바지', 9800)\n",
        "data_add2products(210, '풋살바지', 10500, '바지', 8600)\n",
        "data_add2products(211, '배드민턴바지', 14900, '바지', 11100)\n",
        "data_add2products(212, '스쿼시바지', 6700, '바지', 5000)"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N91WJjRPCbm9"
      },
      "source": [
        "data_add2products(300, '농구상의', 22000, '상의', 16000)\n",
        "data_add2products(301, '탁구상의', 25000, '상의', 20000)\n",
        "data_add2products(302, '축구상의', 32000, '상의', 25000)\n",
        "data_add2products(303, '배구상의', 18000, '상의', 13000)\n",
        "data_add2products(304, '볼링상의', 19500, '상의', 12500)\n",
        "data_add2products(305, '테니스상의', 23900, '상의', 17000)\n",
        "data_add2products(306, '골프상의', 36700, '상의', 24000)\n",
        "data_add2products(307, '런닝상의', 21800, '상의', 16000)\n",
        "data_add2products(308, '야구상의', 29300, '상의', 23700)\n",
        "data_add2products(309, '펜싱상의', 23600, '상의', 14800)\n",
        "data_add2products(310, '풋살상의', 20500, '상의', 15600)\n",
        "data_add2products(311, '배드민턴상의', 24900, '상의', 17100)\n",
        "data_add2products(312, '스쿼시상의', 16700, '상의', 11000)"
      ],
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VMoc55rlDzkF"
      },
      "source": [
        "data_add2sales('2020-2-26', 'NIKE', 100, 50)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rcMvaWXhD631"
      },
      "source": [
        "# 거래내역 한꺼번에 채워넣기\n",
        "import random\n",
        "company_list = ['NIKE', 'ADIDAS', 'MIZUNO', 'UNDERARMOUR', 'NEWBALANCE', 'DESCENTE']\n",
        "prod_cate_list = [1,2,3]\n",
        "for i in range(500):\n",
        "    m = random.randrange(1,13)\n",
        "    d = random.randrange(1,30)\n",
        "    sdate1 = f'2020-{m}-{d}'\n",
        "    scompany1 = random.choice(company_list)\n",
        "    spid1 = random.choice(prod_cate_list)*100+random.randrange(0,13)\n",
        "    sunit1 = random.randrange(10,1000)\n",
        "    data_add2sales(sdate1, scompany1, spid1, sunit1)"
      ],
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GJUaZDzuEM4B"
      },
      "source": [
        "# 월별 매출/이익\n",
        "def month_sales(month):\n",
        "    cur = conn.cursor()\n",
        "    sql_month_sales = '''\n",
        "    SELECT products.pname, products.pprice,\n",
        "    products.pcost, sales.sdate, sales.sunit\n",
        "    FROM products\n",
        "    JOIN sales\n",
        "    ON products.pid=sales.spid\n",
        "    WHERE sales.sdate\n",
        "    BETWEEN '2020-%s-01' AND '2020-%s-29'\n",
        "    ORDER BY sales.sdate;\n",
        "    '''\n",
        "    cur.execute(sql_month_sales, (month, month))\n",
        "    rows = cur.fetchall()\n",
        "    month_sales = 0\n",
        "    for i in range(len(rows)):\n",
        "        month_sales += rows[i][1] * rows[i][-1]\n",
        "    return month_sales\n",
        "\n",
        "\n",
        "def month_profit(month):\n",
        "    cur = conn.cursor()\n",
        "    sql_month_sales = '''\n",
        "    SELECT products.pname, products.pprice,\n",
        "    products.pcost, sales.sdate, sales.sunit\n",
        "    FROM products\n",
        "    JOIN sales\n",
        "    ON products.pid=sales.spid\n",
        "    WHERE sales.sdate\n",
        "    BETWEEN '2020-%s-01' AND '2020-%s-29'\n",
        "    ORDER BY sales.sdate;\n",
        "    '''\n",
        "    cur.execute(sql_month_sales, (month, month))\n",
        "    rows = cur.fetchall()\n",
        "    month_profit = 0\n",
        "    for i in range(len(rows)):\n",
        "        month_profit += (rows[i][1] - rows[i][2]) * rows[i][-1]\n",
        "    return month_profit"
      ],
      "execution_count": 68,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DGg6PuMVQ04c"
      },
      "source": [
        "# 거래처별 매출/이익\n",
        "def scompany_sales(scompany1):\n",
        "    cur = conn.cursor()\n",
        "    sql_scompany_sales = '''\n",
        "    SELECT products.pname, products.pprice,\n",
        "    products.pcost, sales.sdate, sales.sunit\n",
        "    FROM products\n",
        "    JOIN sales\n",
        "    ON products.pid=sales.spid\n",
        "    WHERE sales.scompany=%s\n",
        "    ORDER BY sales.sdate;\n",
        "    '''\n",
        "    cur.execute(sql_scompany_sales, (scompany1,))\n",
        "    rows = cur.fetchall()\n",
        "    scompany_sales = 0\n",
        "    for i in range(len(rows)):\n",
        "        scompany_sales += rows[i][1] * rows[i][-1]\n",
        "    return scompany_sales\n",
        "\n",
        "def scompany_profit(scompany1):\n",
        "    cur = conn.cursor()\n",
        "    sql_scompany_sales = '''\n",
        "    SELECT products.pname, products.pprice,\n",
        "    products.pcost, sales.sdate, sales.sunit\n",
        "    FROM products\n",
        "    JOIN sales\n",
        "    ON products.pid=sales.spid\n",
        "    WHERE sales.scompany=%s\n",
        "    ORDER BY sales.sdate;\n",
        "    '''\n",
        "    cur.execute(sql_scompany_sales, (scompany1,))\n",
        "    rows = cur.fetchall()\n",
        "    scompany_profit = 0\n",
        "    for i in range(len(rows)):\n",
        "        scompany_profit += (rows[i][1] - rows[i][2]) * rows[i][-1]\n",
        "    return scompany_profit"
      ],
      "execution_count": 75,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kPxue2KNRJcZ"
      },
      "source": [
        "# 거래처별 판매제품 및 수량\n",
        "def scompany_product_unit(scompany1, pname1):\n",
        "    cur = conn.cursor()\n",
        "    sql_com_pro_unit = '''\n",
        "    SELECT products.pid, products.pname, products.pprice,\n",
        "    products.pcost, sales.scompany, sales.sunit\n",
        "    FROM products\n",
        "    JOIN sales\n",
        "    ON products.pid=sales.spid\n",
        "    WHERE sales.scompany=%s;\n",
        "    '''\n",
        "    cur.execute(sql_com_pro_unit, (scompany1,))\n",
        "    rows = cur.fetchall()\n",
        "    sum_unit = 0\n",
        "    for i in range(len(rows)):\n",
        "        if rows[i][1] == pname1:\n",
        "            sum_unit += rows[i][-1]\n",
        "    return sum_unit"
      ],
      "execution_count": 87,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sR0eA8llqAk9",
        "outputId": "b4f5dcd0-0d9b-4b3d-a779-7f238ff5017d"
      },
      "source": [
        "# 제품별 판매수량/매출/이익"
      ],
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1477"
            ]
          },
          "metadata": {},
          "execution_count": 88
        }
      ]
    }
  ]
}