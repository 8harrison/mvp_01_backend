import bcrypt
import hmac

KEY_PROVISORIA = 'senha_super_secreta_ponto_com'

class GerenciadorSenhas:
    def __init__(self, fator_custo: int = 14, pepper: str = KEY_PROVISORIA):
        """
        Inicializa o gerenciador de senhas.

        Args: 
            fator_custo: Número de itereções (2^fator_custo).
            pepper: String adicional para aumentar a segurança.
        """
        self.fator_custo = fator_custo
        self.pepper = pepper.encode()

    def _aplicar_pepper(self, senha: str) -> bytes:
        """
        Aplica pepper à senha usando HMAC-SHA256.

        Args:
            senha: Senha em texto plano

        Returns:
            Senha com pepper aplicado
        """
        return hmac.new(self.pepper, senha.encode(), 'sha256').digest()
    
    def criptografar_senha(self, senha: str) -> str:
        """
        Criptografa uma senha usando bcrypt com pepper opcional.
        
        Args:
            senha: Senha em texto plano a ser criptografada
            
        Returns:
            Hash da senha em formato string
        """
        try:
            # Aplica pepper se configurado
            senha_processada = self._aplicar_pepper(senha)
            
            # Gera salt com o fator de custo especificado
            salt = bcrypt.gensalt(rounds=self.fator_custo)
            
            # Gera o hash da senha
            hash_senha = bcrypt.hashpw(senha_processada, salt)
            
            return hash_senha.decode('utf-8')
            
        except Exception as e:
            raise Exception(f"Erro ao criptografar senha: {str(e)}")
    
    def validar_senha(self, senha: str, hash_senha: str) -> bool:
        """
        Valida se uma senha corresponde ao hash armazenado.
        
        Args:
            senha: Senha em texto plano para validar
            hash_senha: Hash da senha armazenada
            
        Returns:
            True se a senha corresponder, False caso contrário
        """
        try:
            # Aplica pepper se configurado
            senha_processada = self._aplicar_pepper(senha)
            
            # Converte o hash para bytes
            hash_bytes = hash_senha.encode('utf-8')
            
            # Verifica se a senha corresponde ao hash
            return bcrypt.checkpw(senha_processada, hash_bytes)
            
        except Exception as e:
            print(f"Erro ao validar senha: {str(e)}")
            return False
    
    