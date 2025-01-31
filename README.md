# Keycloak SAML Configuration for Django Applications

This guide provides the necessary steps to configure **Keycloak** as an **Identity Provider (IdP)** for Django applications using SAML authentication.

---

## **1️⃣ Create a Keycloak Realm**
1. Log in to Keycloak Admin Console (`http://localhost:8080/admin/`).
2. Create a new realm (or use an existing one):
   - Click **Add Realm** → Enter a name (e.g., `saml-project`) → **Save**.

---

## **2️⃣ Create a Client for Django Application**
1. Navigate to **Clients** → **Create**.
2. Enter the following details:
   - **Client ID**: `app1`
   - **Client Protocol**: `saml`
   - **Root URL**: `http://localhost:8001/`

### **Update Client Settings**
- **Valid Redirect URIs**:
  - `http://localhost:8001/saml2/acs/`
- **Base URL**: `http://localhost:8001/`
- **Master SAML Processing URL**: `http://localhost:8001/saml2/`
- **Force POST Binding**: ✅ Checked
- **Include AuthnStatement**: ✅ Checked
- **Sign Assertions**: ✅ Checked
- **Signature Algorithm**: `RSA_SHA256`
- **Encrypt Assertions**: ❌ Unchecked (optional)
- **Client Signature Required**: ✅ Checked
- **Front Channel Logout**: ✅ Checked
- **Backchannel Logout**: ✅ Checked
- **Logout Service Redirect Binding URL**: `http://localhost:8001/saml2/slo/`
- **Logout Service POST Binding URL**: `http://localhost:8001/saml2/slo/`


---

## **3️⃣ Configure SAML Keys and Certificates**
1. Go to the **Keys** tab.
2. Ensure that the signing keys are generated.
3. Download the **SAML Metadata** for the client:
   - Click **Export** → **Download**.
4. Place this metadata file (`idp.xml`) in the Django app directory.

---

## **4️⃣ Configure User Attributes for SAML**
1. Navigate to **Realm Settings** → **General**.
2. Under `SAML Endpoint Compatibility Mode`, select **Keycloak**.
3. Go to **Clients** → `app1` → **Client Scopes**.
4. Add the following attributes:
   - **email** → `email`
   - **username** → `preferred_username`
   - **NameID Format**: `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`


---

## **5️⃣ Configure Single Logout (SLO)**
1. Go to **Clients** → `app1` → **Settings**.
2. Ensure **Logout Service URLs** are correctly set:
   - `http://localhost:8001/saml2/slo/`
3. Under **Advanced Settings**:
   - Enable **Front Channel Logout**.
4. Under **Realm Settings** → **Keys**, ensure signing keys are set up.


---


---

## **Private key and cert**
1. In the **Keys** → keycloak generate cert and private key, private key and x509 certificate comming from sp metadata where validated to proper format for djnago and puted in the files
---

all these steps are same in both client
