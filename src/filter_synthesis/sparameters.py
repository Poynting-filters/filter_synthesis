import numpy as np
def compute_sparameters( M: np.ndarray, Q_e1: float, Q_eN: float, f0: float, BW: float, f: np.ndarray = None, n_points: int = 1000) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute S-parameters (S11, S21) of a coupled-resonator filter from its
    coupling matrix and external quality factors.
 
    Parameters
    ----------
    M : np.ndarray, shape (N, N)
        Normalized coupling matrix. Diagonal entries M_ii are self-coupling
        (resonator frequency offsets); off-diagonal M_ij are inter-resonator
        couplings.
    Q_e1 : float
        External quality factor at the input port (port 1).
    Q_eN : float
        External quality factor at the output port (port N).
    f0 : float
        Center frequency in Hz.
    BW : float
        Bandwidth in Hz (absolute, not fractional).
    f : np.ndarray, optional
        Frequency array in Hz. If None, a default sweep of ±3× BW around f0
        is generated using `n_points` points.
    n_points : int, optional
        Number of frequency points when `f` is not provided. Default is 1000.
 
    Returns
    -------
    f : np.ndarray
        Frequency array in Hz.
    S11 : np.ndarray (complex)
        Reflection coefficient at port 1.
    S21 : np.ndarray (complex)
        Transmission coefficient from port 1 to port N.
 
    Notes
    -----
    The normalized low-pass frequency variable is:
        Omega = (f0 / BW) * (f / f0 - f0 / f)
 
    The generalized N×N matrix at each frequency is:
        A = Omega * I - M + j * Q_inv
    where Q_inv has non-zero entries only at [0,0] = 1/Q_e1 and [N-1,N-1] = 1/Q_eN.
 
    S-parameters are then:
        S21 = -2j / sqrt(Q_e1 * Q_eN) * inv(A)[N-1, 0]
        S11 =  1  + (2j / Q_e1)        * inv(A)[0,   0]
    """
    M = np.asarray(M, dtype=complex)
    N = M.shape[0]
    if M.shape != (N, N):
        raise ValueError(f"M must be a square matrix, got shape {M.shape}.")
    if N < 2:
        raise ValueError("Coupling matrix must be at least 2×2.")
 
    # Build default frequency sweep if not provided
    if f is None:
        f = np.linspace(f0 - 3 * BW, f0 + 3 * BW, n_points)
    f = np.asarray(f, dtype=float)
 
    # Normalized low-pass frequency variable
    Omega = (f0 / BW) * (f / f0 - f0 / f)
 
    # Sparse external Q matrix (only corners populated)
    Q_inv = np.zeros((N, N), dtype=complex)
    Q_inv[0,   0  ] = 1.0 / Q_e1
    Q_inv[N-1, N-1] = 1.0 / Q_eN
 
    # Pre-allocate output arrays
    S11 = np.zeros(len(f), dtype=complex)
    S21 = np.zeros(len(f), dtype=complex)
 
    # Identity matrix
    I = np.eye(N, dtype=complex)
 
    # Sweep over frequency
    for k, Om in enumerate(Omega):
        A = Om * I - M + 1j * Q_inv
        A_inv = np.linalg.inv(A)
        S21[k] = -2j / np.sqrt(Q_e1 * Q_eN) * A_inv[N-1, 0]
        S11[k] =  1  + (-2j / Q_e1)           * A_inv[0,   0]
 
    return f, S11, S21