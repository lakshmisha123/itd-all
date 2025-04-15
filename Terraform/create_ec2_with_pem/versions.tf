terraform {
    required_version = ">=1.5.0, < 2.0.0"

    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = ">=5.0, < 6.0"
        }
    }

    backend "s3" {
        
    }

}