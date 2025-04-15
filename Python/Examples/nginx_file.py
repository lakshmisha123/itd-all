import os


def generate_nginx_config(proxy_pass, domain_names, ssl_cert_path, ssl_key_path):
    domain_names_str = " ".join(domain_names)
    config = f"""
    server {{
        listen 80;
        listen 443 ssl;
        server_name {domain_names_str};

        ssl_certificate {ssl_cert_path};
        ssl_certificate_key {ssl_key_path};

        location / {{
            proxy_pass {proxy_pass};
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }}
    }}
    """
    config_filename = f"/etc/nginx/sites-available/{domain_names[0]}.conf"
    with open(config_filename, "w") as file:
        file.write(config)

    # Create a symbolic link to enable the site
    enabled_config_filename = f"/etc/nginx/sites-enabled/{domain_names[0]}.conf"
    os.symlink(config_filename, enabled_config_filename)
    print(f"Nginx configuration created: {config_filename}")


# Example usage
generate_nginx_config("http://127.0.0.1:8000", ["example.com", "www.example.com"], "/path/to/ssl_certificate.crt",
                      "/path/to/ssl_certificate.key")
