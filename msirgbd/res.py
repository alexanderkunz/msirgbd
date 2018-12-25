
INDEX = """

<html>
    <head>
        <meta name="viewport" content="width=device-width"/>
        <title>MSI-RGB Daemon</title>
    </head>
    
    <style>
    
        body {
            background-color: black;
            color: white;
        }
        
        .set {
            font-size: 10px;
            margin: 4px 2px;
            border: 2px solid #696969;
            border-radius: 2px;
            background-color: #009900;
        }

        .reset {
            background-color: grey;
            color: white;
        }
        .button {
            color: black;
            padding: 4px 8px;
            font-size: 16px;
            margin: 4px 2px;
            width: 100%;
            cursor: pointer;
            display: inline-block;
        }

        .head {
            color: black;
            padding: 5px 11px;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            display: inline-block;
            border: 2px solid #696969;
            border-radius: 8px;
            background-color: #e7e7e7e7;
        }

        .blue {
            background-color: #000099;
            color: white;
        }

        .green {
            background-color: #009900;
            color: white;
        }

        .red {
            background-color: #cc0000;
            color: white;
        }
        
        .yellow {
            background-color: #FFD800;
        }

        .b_blue {
            background-color: white;
            color: black;
            border: 2px solid #000099;
        }

        .b_green {
            background-color: white;
            color: black;
            border: 2px solid #009900;
        }

        .b_red {
            background-color: white;
            color: black;
            border: 2px solid #cc0000;
        }
        
        .b_yellow {
            background-color: white;
            color: black;
            border: 2px solid #FFD800;
        }
        
        .b_white {
            background-color: white;
            color: black;
            border: 2px solid #FFFFFF;
        }

        .active {
            background-color: grey;
        }
        
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            padding-top: 100px;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0,0,0);
            background-color: rgba(0,0,0,0.4);
        }
        
        .modal-content {
            background-color: grey;
            margin: auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
        }
        
        .close {
            color: #aaaaaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        
        .close:hover,
        .close:focus {
            color: #000;
            text-decoration: none;
            cursor: pointer;
        }

        .popup {}
    </style>
    <body>
    
        <h3>Static Color</h3>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/0/0/0/0'" class="head" value="Off">
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/255/0/0/0'" class="head b_red" value="Red255">
                    <input type=button onClick="location.href='/color/0/255/0/0'" class="head b_green" value="Green255">
                    <input type=button onClick="location.href='/color/0/0/255/0'" class="head b_blue" value="Blue255">
                    <input type=button onClick="location.href='/color/255/255/255/0'" class="head b_white" value="White255">
                    <input type=button onClick="location.href='/color/255/255/0/0'" class="head b_yellow" value="Yellow255">
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/64/0/0/0'" class="head b_red" value="Red64">
                    <input type=button onClick="location.href='/color/0/64/0/0'" class="head b_green" value="Green64">
                    <input type=button onClick="location.href='/color/0/0/64/0'" class="head b_blue" value="Blue64">
                    <input type=button onClick="location.href='/color/64/64/64/0'" class="head b_white" value="White64">
                    <input type=button onClick="location.href='/color/64/64/0/0'" class="head b_yellow" value="Yellow64">
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/16/0/0/0'" class="head b_red" value="Red16">
                    <input type=button onClick="location.href='/color/0/16/0/0'" class="head b_green" value="Green16">
                    <input type=button onClick="location.href='/color/0/0/16/0'" class="head b_blue" value="Blue16">
                    <input type=button onClick="location.href='/color/16/16/16/0'" class="head b_white" value="White16">
                    <input type=button onClick="location.href='/color/16/16/0/0'" class="head b_yellow" value="Yellow16">
                </td>
            </tr>
        </table>
        
        <h3>Static Color (Pulse)</h3>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/255/0/0/1'" class="head b_red" value="Red255">
                    <input type=button onClick="location.href='/color/0/255/0/1'" class="head b_green" value="Green255">
                    <input type=button onClick="location.href='/color/0/0/255/1'" class="head b_blue" value="Blue255">
                    <input type=button onClick="location.href='/color/255/255/255/1'" class="head b_white" value="White255">
                    <input type=button onClick="location.href='/color/255/255/0/1'" class="head b_yellow" value="Yellow255">
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/64/0/0/1'" class="head b_red" value="Red64">
                    <input type=button onClick="location.href='/color/0/64/0/1'" class="head b_green" value="Green64">
                    <input type=button onClick="location.href='/color/0/0/64/1'" class="head b_blue" value="Blue64">
                    <input type=button onClick="location.href='/color/64/64/64/1'" class="head b_white" value="White64">
                    <input type=button onClick="location.href='/color/64/64/0/1'" class="head b_yellow" value="Yellow64">
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/color/16/0/0/1'" class="head b_red" value="Red16">
                    <input type=button onClick="location.href='/color/0/16/0/1'" class="head b_green" value="Green16">
                    <input type=button onClick="location.href='/color/0/0/16/1'" class="head b_blue" value="Blue16">
                    <input type=button onClick="location.href='/color/16/16/16/1'" class="head b_white" value="White16">
                    <input type=button onClick="location.href='/color/16/16/0/1'" class="head b_yellow" value="Yellow16">
                </td>
            </tr>
        </table>
        
        <h3>Hue Wheel</h3>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/hue/1'" class="head b_green" value="Slow">
                    <input type=button onClick="location.href='/hue/10'" class="head b_green" value="Normal">
                    <input type=button onClick="location.href='/hue/25'" class="head b_green" value="Fast">
                    <input type=button onClick="location.href='/hue/100'" class="head b_red" value="Insane">
                </td>
            </tr>
        </table>
        
        <h3>Misc</h3>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/heartbeat'" class="head b_yellow" value="Heartbeat">
                    <input type=button onClick="location.href='/police'" class="head b_yellow" value="Police">
                    <input type=button onClick="location.href='/easter'" class="head b_yellow" value="Happy Easter">
                </td>
            </tr>
        </table>
        
        <h3>Perlin</h3>
        <table>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/perlin/70/255/0/0'" class="head b_red" value="Red255">
                    <input type=button onClick="location.href='/perlin/70/0/255/0'" class="head b_green" value="Green255">
                    <input type=button onClick="location.href='/perlin/70/0/0/255'" class="head b_blue" value="Blue255">
                    <input type=button onClick="location.href='/perlin/70/255/255/255'" class="head b_white" value="White255">
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <input type=button onClick="location.href='/perlin/20/255/255/0'" class="head b_red" value="RedGreen255">
                    <input type=button onClick="location.href='/perlin/20/0/255/255'" class="head b_red" value="GreenBlue255">
                    <input type=button onClick="location.href='/perlin/20/255/0/255'" class="head b_red" value="RedBlue255">
                </td>
            </tr>
        </table>
        
    </body>
</html>
"""
