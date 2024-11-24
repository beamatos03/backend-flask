reset_password_email_html_content = """
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #f4f4f9;
            padding: 20px;
        }
        .email-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #2B5FB5;
        }
        p {
            font-size: 16px;
            line-height: 1.5;
        }
        a{
            text-decoration: none;
            font-weight: bold;
        }
        .button{
            color: #ffffff;
            display: inline-block;
            background-color: #6b91ce;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            border-radius: 4px;
            font-size: 16px;
            margin-top: 20px;
            color: white;
        }
        .footer{
            text-align: center;
            font-size: 12px;
            color: #888;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <h2>Olá,</h2>
        <p>Você está recebendo este e-mail porque solicitou a redefinição da senha da sua conta.</p>
        
        <p>Para redefinir sua senha, clique no link abaixo:</p>
        <a href="{{ reset_password_url }}" class="button">Redefinir Senha</a>
        
        <p>Ou copie e cole o seguinte link na barra de endereços do seu navegador:</p>
        <p><a href="{{ reset_password_url }}">{{ reset_password_url }}</a></p>
        
        <p>Se você não fez essa solicitação, por favor, ignore este e-mail ou entre em contato com a nossa equipe.</p>
        
        <p>Obrigado!</p>
        
        <div class="footer">
            <p>Este é um e-mail automático, por favor não responda.</p>
        </div>
    </div>
</body>
</html>
"""
